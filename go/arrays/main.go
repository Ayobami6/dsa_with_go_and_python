package main

import (
	"fmt"
)

func main() {
	arrays := [...]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	results := removeDuplicates(arrays[:])
	fmt.Println(results)

	prices := [...]int{7, 1, 5, 3, 6, 4}
	profit := bestTimeToBuyStocks(prices[:])
	fmt.Println(profit)

	digits := []int{4, 3, 2, 1}
	result := plusOne(digits)
	fmt.Println(result)

}

// bestTimeToBuyStocks coding challenge solution
func bestTimeToBuyStocks(prices []int) int {
	maxProfit := 0
	newPrices := prices[:len(prices)-1]
	for i, _ := range newPrices {
		// check if current price is less than the next price
		if prices[i] < prices[i+1] {
			// buy the stock, so as to sell the next day with lesser price
			profit := prices[i+1] - prices[i]
			maxProfit += profit

		}
	}
	return maxProfit

}

func removeDuplicates(nums []int) int {
	unique := 0
	for i, _ := range nums {
		if nums[i] != nums[unique] {
			nums[unique+1] = nums[i]
			// increment unique
			unique++

		}
	}
	return unique + 1

}

func plusOne(digits []int) []int {
	n := len(digits)
	for i := n - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	return append([]int{1}, digits...)

}
