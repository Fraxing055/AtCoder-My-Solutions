import std.stdio;
import std.string;
import std.conv;
import std.algorithm;
import std.array;
import std.range;
import std.math;

void main() {
  auto N = readln().chomp().to!int;
  writeln(2 ^^ N - N * 2);
}
