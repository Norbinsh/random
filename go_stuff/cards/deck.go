// Part of https://www.udemy.com/go-the-complete-developers-guide/
// This package exposes a deck type with some functions allowing you
// to create and modify deck of cards
package main

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"strings"
	"time"
)

// create a new type of 'deck'
// which is basically just a slice of strings
// a slice is basically just a segment of standard array, that is provides
// more power and flexibility.
type deck []string

// creates a new deck, returns a "deck-slice"
func newDeck() deck {
	cards := deck{}

	cardsSuits := []string{"Spades", "Diamonds", "Hearts", "Clubs"}
	cardsValues := []string{"Ace", "Two", "Three", "Four"}

	for _, suit := range cardsSuits {
		for _, value := range cardsValues {
			cards = append(cards, value+" of "+suit)
		}
	}

	return cards
}

// prints out each index + card in the deck
// notice the use of a reciver function below
// reciver basically allows you to add methods to any variables of the
// given type, so in the example below we add the "print" method to:
// d variable of type deck.
func (d deck) print() {
	for i, card := range d {
		fmt.Println(i, card)
	}
}

// again a reciver function, adding 'shuffle' method to our deck
// notice how we first randomize a source using current unix time, that
// is then used as a seed for the rand type.
// Otherwise, and by default - same seed is used.
func (d deck) shuffle() {

	source := rand.NewSource(time.Now().Unix())
	r := rand.New(source)

	for i := range d {
		newPosition := r.Intn(len(d) - 1)
		d[i], d[newPosition] = d[newPosition], d[i]

	}
}

// deal gets 2 arguments: deck & int, and returns 2 sliced decks
func deal(d deck, handSize int) (deck, deck) {
	return d[:handSize], d[handSize:]
}

// concatenates the deck values into a single string while adding a
// separator between each value, in this case the seprator is ",""
func (d deck) toString() string {
	return strings.Join([]string(d), ",")
}

// IOPS! using the ioutil package we are writing the content of the deck into a file.
// notice how we convert the deck into a string -> into bytes, as required by the
// WriteFile method which takes data as bytes.
// the number at the end is just the chmod / file permissions (although i am on windows now...)
// so 0666 would stand for: 0 -> UID root -> read+write for user/group/others.
func (d deck) saveToFile(filename string) error {
	return ioutil.WriteFile(filename, []byte(d.toString()), 0666)
}

// see how ReadFile returns 2 things - if the err returned by it is anything other
// than nil, something  went wrong, we'll use the os package to exit with a code of
// 1 to signal something went wrong.
// nil in go is the "zero value" for pointers/interfaces/maps/slices/channels and
// function types, it basically represent a value that was not initialized.
// by zero value is what a variable gets by default when it wasn't explicitly given
// a value... so the zero value of "var num int" is 0, since 0 is the zero value of
// the int type.
func newDeckFromFile(filename string) deck {
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}

	s := strings.Split(string(content), ",")
	return deck(s)
}
