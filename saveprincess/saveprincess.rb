#!/bin/ruby

def displayPathtoPrincess(m, grid)
  maze = grid.map! { |x| x.split("") }
  search(maze)
end

def search(maze)
  start, ending = nil, nil
  for i in 0...maze.length
    for j in 0...maze.length
      l = maze[i][j]
      if l == 'm'
        start = [i, j]
      elsif l == 'p'
        ending = [i, j]
      end
    end
    if not start.nil? and not ending.nil?
      break
    end
  end

  while true
    cmp = start[0] <=> ending[0]
    if cmp == 0
      break
    elsif cmp > 0
      puts "UP"
    else
      puts "DOWN"
    end
  end

  while true
    cmp = start[1] <=> ending[1]
    if cmp == 0
      break
    elsif cmp > 0
      puts "LEFT"
    else
      puts "RIGHT"
    end
  end

end
