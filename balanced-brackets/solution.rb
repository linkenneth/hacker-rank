#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

MATCHES = {
  '}' => '{',
  ']' => '[',
  ')' => '('
}

def isBalanced(s)
  stack = []
  s.each_char do |c|
    case c
    when '{', '[', '('
      stack.push(c)
    when '}', ']', ')'
      unless MATCHES[c] == stack.pop
        return 'NO'
      end
    end
  end
  stack.length == 0 ? 'YES' : 'NO'
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

t = gets.strip.to_i

t.times do |t_itr|
    s = gets.chomp

    result = isBalanced s

    fptr.write result
    fptr.write "\n"
end

fptr.close()
