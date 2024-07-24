#include <iostream>
#include <set>

using namespace std;

int main(){
    set<int> alunos;
    int n, x;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> x;
        alunos.insert(x);
    }
    cout << alunos.size() << endl;
}
