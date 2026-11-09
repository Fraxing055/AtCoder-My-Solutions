import std.stdio;
import std.string;
import std.conv;
import std.array;

void main() {
  auto tokens = readln().split();
  int H = tokens[0].to!int();
  int W = tokens[1].to!int();
  string ans = "";
  string C = "";
  for (int i=0; i<H; i++) {
    C = readln().chomp();
    writeln(C ~ '\n' ~ C);
  };
}
