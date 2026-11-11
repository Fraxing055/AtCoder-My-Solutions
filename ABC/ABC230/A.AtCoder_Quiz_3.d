import std.stdio;
import std.string;
import std.conv;
import std.algorithm;
import std.array;
import std.range;
import std.math;

void main() {
  int N = readln().chomp().to!int;
  int ans = 0;
  if (N < 42) {
    ans = N;
  } else {
    ans = N + 1;
  }
  if (ans < 10) {
    writeln("AGC00" ~ ans.to!string);
  } else {
    writeln("AGC0" ~ ans.to!string);
  }
}
