package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	f, _ := os.Open("input1.txt")
	scanner := bufio.NewScanner(f)
	var inp []int
	for scanner.Scan() {
		line := scanner.Text()
		num, _ := strconv.Atoi(line)
		inp = append(inp, num)

	}

	// part 1
	count := 0
	for i := 1; i < len(inp); i++ {
		if inp[i] > inp[i-1] {
			count++
		}
	}
	fmt.Println(count)

	// part 2
	count = 0
	for i := 3; i < len(inp); i++ {
		if inp[i-3] < inp[i] {
			count++
		}
	}
	fmt.Println(count)
}
