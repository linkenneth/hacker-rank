#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s)
  chars = s.chars.reject { |c| c == ' ' }
  ceil = Math.sqrt(chars.size).ceil
  grid = chars.each_slice(ceil).to_a
  grid[0].size.times.map do |c|
    grid.size.times.map { |r| grid[r][c] }.compact.join
  end.join(' ')
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

s = gets.chomp

result = encryption s

fptr.write result
fptr.write "\n"

fptr.close()
