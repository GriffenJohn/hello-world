#include <stdlib.h>

typedef struct __node
{
  int data;
  struct __node *next;
} node;

node *node_create(int data)
{
  node *node = malloc(sizeof(node));
  if(node)
  {
    node->data = data;
    node->next = NULL;
  }
  return node;
}

