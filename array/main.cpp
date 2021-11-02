#include <stdio.h>
# include <stdlib.h>

struct Arr{
    int * pBase;    //数组存储的第一个元素地址, 数组首地址
    int len;    //数组的长度
    int cnt;    //当前数组内已有的元素长度
};
void init_arr(struct Arr *pArr, int length);
bool append_arr(struct Arr *pArr, int val);  //末尾追加一个
bool insert_arr(struct Arr *pArr, int pos, int val);  //插入
bool delete_arr();
int get();
bool is_empty(struct Arr * pArr);
bool is_full(struct Arr * pArr);
void sort_arr();
void show_arr(struct Arr * pArr);   //传一个引用
void inversion();   //倒置

int main(void) {
    struct Arr arr;
    init_arr(&arr, 6);
    append_arr(&arr, 1);
    append_arr(&arr, 2);
    append_arr(&arr, 3);
    append_arr(&arr, 4);
    append_arr(&arr, 5);
    show_arr(&arr);
    return 0;
}

void init_arr(struct Arr *pArr, int length){
    pArr->pBase = (int *)malloc(sizeof(int) * length);
    if(NULL == pArr->pBase)
    {
        printf("动态内存分配失败！");
        exit(-1);
    }
    else
    {
        pArr->len = length;
        pArr->cnt = 0;
    }
    return;
}

void show_arr(struct Arr * pArr){    // pArr是结构体变量的地址
    if(is_empty(pArr))
    {
        printf("数组为空！");
    }
    else
    {
        for (int i=0; i<pArr->cnt; ++i){
            printf("%d", pArr->pBase[i]);
            printf("\r\n");
        }
    }
}

bool is_empty(struct Arr * pArr){
    if(0 == pArr->cnt){
        return true;
    }
    else
    {
        return false;
    }
}

bool is_full(struct Arr * pArr){
    if(pArr->cnt == pArr->len)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool append_arr(struct Arr * pArr, int val){
    if(is_full(pArr)){
        return false;   //数组满了
    }
    else
    {
        pArr->pBase[pArr->cnt] = val;
        pArr->cnt++;
        return true;
    }
}