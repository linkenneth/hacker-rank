require 'set'

def pairs(nums, k)
  s = nums.to_set
  count = 0
  nums.each do |n|
    count += (s.include? (n + k)) ? 1 : 0
  end
  puts count
end

n, k = gets.chomp.split.map &:to_i
nums = gets.chomp.split.map &:to_i
pairs(nums, k)
