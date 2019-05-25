// Part of https://www.udemy.com/go-the-complete-developers-guide/
// This package provides several basic tests to make sure the deck
// package is behaving correctly
// notice the name of this file - any test package in go should end with
// _test.go.
package main

import (
	"os"
	"testing"
)

// CamelCase convention, including an UPPER first letter for test functions
func TestNewDeck(t *testing.T) {
	d := newDeck()

	if len(d) != 16 {
		t.Errorf("Expected deck length of 16, but got %v", len(d))
	}

	if d[0] != "Ace of Spades" {
		t.Errorf("First card is not as expected (Ace of Spades), instead got: %v", d[0])
	}

	if d[len(d)-1] != "Four of Clubs" {
		t.Errorf("Last card is not as expected (Four of Clubs), instead got: %v", d[len(d)-1])
	}
}

func TestSaveToFileAndNewDeckFromFile(t *testing.T) {
	os.Remove("_decktesting")

	deck := newDeck()

	deck.saveToFile("_decktesting")

	loadedDeck := newDeckFromFile("_decktesting")

	if len(loadedDeck) != 16 {
		t.Errorf("Expected 16 cards in deck but got %v", len(loadedDeck))
	}

	os.Remove("_decktesting")
}
