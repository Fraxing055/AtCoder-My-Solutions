import std.stdio;
import std.string;
import std.conv;
import std.algorithm;
import std.array;
import std.range;
import std.math;

void main() {
  int A, B, C;
  readf(" %d %d %d", &A, &B, &C);
  if (A + B == C) {writeln("Yes");}
  else {writeln("No");}
}
