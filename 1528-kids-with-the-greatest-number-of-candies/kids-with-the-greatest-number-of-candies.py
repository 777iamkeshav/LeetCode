class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		high_enough = max(candies) - extraCandies
		result = []
		for num in candies:
			result.append(num >= high_enough)
		return result