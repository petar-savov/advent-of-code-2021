package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, _ := os.Open("input2.txt")

	// part 1
	h, d := 0, 0
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		line := scanner.Text()
		x, _ := strconv.Atoi(string(line[len(line)-1]))
		if strings.HasPrefix(line, "down") {
			d += x
		} else if strings.HasPrefix(line, "up") {
			d -= x
		} else {
			h += x
		}
	}
	fmt.Println(h * d)
	f.Close()

	// part 2
	h, d, aim := 0, 0, 0
	f, _ = os.Open("input2.txt")
	scanner = bufio.NewScanner(f)

	for scanner.Scan() {
		line := scanner.Text()
		x, _ := strconv.Atoi(string(line[len(line)-1]))
		if strings.HasPrefix(line, "down") {
			aim += x
		} else if strings.HasPrefix(line, "up") {
			aim -= x
		} else {
			h += x
			d += aim * x
		}

	}
	fmt.Println(h * d)
	f.Close()
}
