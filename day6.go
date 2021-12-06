package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
)

func main() {

	inp, _ := ioutil.ReadFile("input6.txt")
	var nums []int

	for _, n := range inp {
		if string(n) != "," && string(n) != "\n" {
			str, _ := strconv.Atoi(string(n))
			nums = append(nums, str)
		}
	}

	var track [9]int
	for _, n := range nums {
		track[n] += 1
	}

	for i := 0; i < 256; i++ {
		new := track[0]
		for j := 0; j < 8; j++ {
			track[j] = track[j+1]
		}
		track[8] = new
		track[6] += new
	}

	s := 0
	for _, n := range track {
		s += n
	}
	fmt.Println(s)

}
