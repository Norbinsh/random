package main

import "fmt"

func main() {
	cards := newDeck()
	fmt.Println(cards)
	x := cards.toString()
	fmt.Println(x)
}
