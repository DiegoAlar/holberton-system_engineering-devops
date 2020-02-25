#!/usr/bin/env ruby
puts ARGV[0].scan(/(Google|\+?\d{11}|-\d:\d:-\d:-?\d:-\d)/).join(',')
