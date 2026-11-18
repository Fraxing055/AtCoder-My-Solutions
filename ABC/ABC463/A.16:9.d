import std.stdio;
import std.string;
import std.conv;
import std.algorithm;
import std.array;
import std.range;
import std.math;

void main() {
  int X, Y;
  readf(" %d %d", &X, &Y);
  writeln(X * 9 == Y * 16 ? "Yes" : "No");
}
