#include <algorithm>
#include <iostream>
#define MAX 10000

using namespace std;

struct Consulta {
    int inicio;
    int fim;
} consultas[MAX];

bool compara(Consulta a, Consulta b) {
    return a.fim < b.fim;
}

int main() {
    int n, qtd = 1;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> consultas[i].inicio >> consultas[i].fim;
    }

    sort(consultas, consultas + n, compara);

    int fim = consultas[0].fim;

    for (int i = 1; i < n; i++) {
        if (consultas[i].inicio >= fim) {
            fim = consultas[i].fim;
            qtd++;
        }
    }

    cout << qtd << endl;
}