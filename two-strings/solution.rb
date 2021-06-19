#!/bin/ruby

require 'json'
require 'stringio'
require 'set'

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2)
  s = s1.split('').to_set
  s2.each_char do |c|
    return 'YES' if s.include?(c)
  end
  'NO'
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

q = gets.strip.to_i

q.times do |q_itr|
    s1 = gets.chomp

    s2 = gets.chomp

    result = twoStrings s1, s2

    fptr.write result
    fptr.write "\n"
end

fptr.close()
