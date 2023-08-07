#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
enum class Token { NUMBER, ID, IF, THEN, ELSE, RELOP };

bool check_Number(string token) {
  if (!isdigit(token[0]))
    return false;
  for (auto c : token) {
  }
}

bool check_Identifier(string token) {
  if (!isalpha(token[0]))
    return false;
  for (char c : token) {
    if (!isalnum(c))
      return false;
  }
  return true;
}

Token *type_Token(string token) {
  Token *token_type;
  if (token == "if") {
    token_type = new Token(Token::IF);
    cout << "if\n";
  } else if (token == "then") {
    token_type = new Token(Token::THEN);
    cout << "then\n";
  } else if (token == "else") {
    token_type = new Token(Token::ELSE);
    cout << "else\n";
  } else if (token == "<" || token == ">" || token == "<=" || token == ">=" ||
             token == "=" || token == "<>") {
    token_type = new Token(Token::RELOP);
    cout << "relop\n";
  } else if (check_Identifier(token)) {
    token_type = new Token(Token::ID);
    std::cout << "id" << std::endl;
  } else if (check_Number(token)) {
    token_type = new Token(Token::NUMBER);
    std::cout << "number" << std::endl;
  } else {
    std::cout << "invalid token" << std::endl;
  }
  return token_type;
}

vector<string> tokenizer(string input) {
  vector<string> tokens;
  int i = 0, o = 0;
  while (i < input.length()) {
    char c = input[i];
    if (c == ' ') {
      tokens.push_back(input.substr(o, (i - o)));
      o = i + 1;
    }
    i++;
  }
  tokens.push_back(input.substr(o));
  return tokens;
}

void processInput(string input) {
  int i = 0;
  int len = input.length();
  while (i < len) {
    c = input[i];
  }
}

// void print_token(Token type_token) { cout << type_token << "\n"; }
int main(void) {
  string input;
  std::cout << "Enter the input string\n" << std::endl;
  getline(cin, input);
  vector<string> tokens = tokenizer(input);
  for (string token : tokens) {
    // cout << token;
    Token *token_type = type_Token(token);
  }
  return 0;
}
