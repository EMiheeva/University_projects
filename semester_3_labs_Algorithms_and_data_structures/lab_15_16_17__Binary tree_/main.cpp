#include <iostream>
#include <fstream>
#include <sstream>
#include <stack>
#include <vector>
struct Elem
{
    int data;
    Elem* left;
    Elem* right;
    Elem* parent;
};

Elem* MAKE(int data, Elem* p)
{
    Elem* q = new Elem;
    q->data = data;
    q->left = nullptr;
    q->right = nullptr;
    q->parent = p;
    return q;
}

Elem* ADD(int data, Elem*& root)
{
    if (root == nullptr) {
        root = MAKE(data, nullptr);
        return root;
    }
    Elem* v = root;
    while ((data < v->data && v->left != nullptr) || (data > v->data && v->right != nullptr))
        if (data < v->data)
            v = v->left;
        else
            v = v->right;
    if (data == v->data)
        return nullptr;
    Elem* u = MAKE(data, v);
    if (data < v->data)
        v->left = u;
    else
        v->right = u;
    return u;
}

Elem* SEARCH(int data, Elem* v)
{
    if (v == nullptr)
        return v;
    if (v->data == data)
        return v;
    if (data < v->data)
        return SEARCH(data, v->left);
    else
        return SEARCH(data, v->right);
}

int DEEP(Elem* v, int digit)
{
    int deep = 1;
    Elem* p = SEARCH(digit, v);

    if (p != nullptr)
    {
        if (v->data == digit)
            return deep;

        while (v->data != digit)
        {
            if (v->data < digit)
                v = v->right;

            else
                v = v->left;
            deep++;
        }
        return deep;
    }
    else
        return deep = 0;
}

void DELETE(int data, Elem*& root)
{

    Elem* u = SEARCH(data, root);
    if (u == nullptr)
        return;

    if (u->left == nullptr && u->right == nullptr && u == root)
    {
        delete root;
        root = nullptr;
        return;
    }

    if (u->left == nullptr && u->right != nullptr && u == root)
    {
        Elem* t = u->right;
        while (t->left != nullptr)
            t = t->left;
        u->data = t->data;
        u = t;
    }

    if (u->left != nullptr && u->right == nullptr && u == root)
    {
        Elem* t = u->left;
        while (t->right != nullptr)
            t = t->right;
        u->data = t->data;
        u = t;
    }

    if (u->left != nullptr && u->right != nullptr)
    {
        Elem* t = u->right;
        while (t->left != nullptr)
            t = t->left;
        u->data = t->data;
        u = t;
    }
    Elem* t;
    if (u->left == nullptr)
        t = u->right;
    else
        t = u->left;
    if (u->parent->left == u)
        u->parent->left = t;
    else
        u->parent->right = t;
    if (t != nullptr)
        t->parent = u->parent;
    delete u;
}

void CLEAR(Elem*& v)
{
    if (v == nullptr)
        return;
    CLEAR(v->left);
    CLEAR(v->right);
    delete v;
    v = nullptr;
}

std::ifstream in("input.txt");
float number() {
    float exp = 0;
    for (;;) {
        char sym = in.get();
        if (sym >= '0' && sym <= '9') {
            exp = exp * 10 + sym - '0';
        }
        else {
            in.putback(sym);
            return exp;
        }

    }
}

void TREE(Elem*& root) {
    Elem* tec = ADD(number(), root);
    char sym = in.get();
    if (sym == '(') {
        sym = in.get();
        if (sym >= '0' && sym <= '9') {
            in.putback(sym);
            TREE(tec);
            sym = in.get();
        }
        if (sym == ',') {
            sym = in.get();
            if (sym >= '0' && sym <= '9')
            {
                in.putback(sym);
                TREE(tec);
                sym = in.get();
            }
        }
        if (sym == ')') {
            return;
        }
    }
    else {
        in.putback(sym);
        return;
    }
}

void PAINT_TREE(Elem*& root) {
    std::cout << "(";
    if (root->left != nullptr)
    {
        std::cout << root->left->data;
        if ((root->left->left != nullptr) || (root->left->right != nullptr))
            PAINT_TREE(root->left);
    }
    std::cout << ',';
    if (root->right != nullptr)
    {
        std::cout << root->right->data;
        if ((root->right->left != nullptr) || (root->right->right != nullptr))
            PAINT_TREE(root->right);
    }
    std::cout << ")";
}

void CENTER(Elem*& root) {
    if (root->left != nullptr) {
        CENTER(root->left);
    }

    std::cout << root->data << " ";

    if (root->right != nullptr) {
        CENTER(root->right);
    }
}
void STRAIGHT(Elem*& root) {
    std::cout << root->data << " ";
    if (root->left != nullptr) {
        STRAIGHT(root->left);
    }

    if (root->right != nullptr) {
        STRAIGHT(root->right);
    }
}
void REVERSED(Elem*& root) {
    if (root->left != nullptr) {
        REVERSED(root->left);
    }

    if (root->right != nullptr) {
        REVERSED(root->right);
    }
    std::cout << root->data << " ";
}
void NOT_RECURSIVE(Elem*& root) {
    int x;
    std::stack<Elem*> s;
    s.push(root);
    while (s.empty() == false) {
        Elem* t = s.top();
        s.pop();
        std::cout << t->data << " ";
        if (t->right) s.push(t->right);
        if (t->left) s.push(t->left);
    }
}

int main()
{
    setlocale(LC_ALL, "Rus");
    Elem* root = nullptr;
    std::ifstream in("input.txt");

    if (!in.is_open())
    {
        std::cout << "File not found" << std::endl;
        return -1;
    }
    char symbol;
    int i;
    TREE(root);

    std::cout << root->data;
    PAINT_TREE(root);
    std::string x;
    std::cout << std::endl << "Центральный обход: ";
    CENTER(root);
    std::cout << std::endl << "Прямой обход: ";
    STRAIGHT(root);
    std::cout << std::endl << "Обратный обход: ";
    REVERSED(root);
    std::cout << std::endl << "Не рекурсивный прямой обход: ";
    NOT_RECURSIVE(root);
    std::cout << std::endl << "Введите ADD x для добавления элемента x, DELETE x для удаления элемента x, SEARCH x для поиска глубины элемента x" << std::endl;
    while (x != "END")
    {
        if (x == "DELETE") {
            std::cin >> i;
            DELETE(i, root);

            std::cout << root->data;
            PAINT_TREE(root);

            std::cout << std::endl << "Введите ADD x для добавления элемента x, DELETE x для удаления элемента x, SEARCH x для поиска глубины элемента x" << std::endl;
        }
        if (x == "ADD")
        {
            std::cin >> i;
            ADD(i, root);

            std::cout << root->data;
            PAINT_TREE(root);

            std::cout << std::endl << "Введите ADD x для добавления элемента x, DELETE x для удаления элемента x, SEARCH x для поиска глубины элемента x" << std::endl;
        }

        if (x == "SEARCH")
        {
            std::cin >> i;
            if ((DEEP(root, i)) == 0)
            {
                std::cout << "Нет элемента";
            }
            else
            {
                std::cout << (DEEP(root, i));
            }
            std::cout << std::endl << "Введите ADD x для добавления элемента x, DELETE x для удаления элемента x, SEARCH x для поиска глубины элемента x" << std::endl;
        }
        std::cin >> x;
    }
    return 0;
}

