/*
--------------------------------
Developed by                    |
user: Dennis Masaya             |
id: 201503413                   |
e-mail: dennismasaya@gmail.com  |
--------------------------------
This example demonstrates how to build a linked list, we use 
2 classes: 1) Node_single and 2)LinkedList, our node class only 
has the attributes and a constructor to add value to those attributes, 
and our LinkeList class has 2 methods (more can be easily implemented) 
1)add and 2)print_list which are self-explanatory, finally on our setup 
method we create, add elements and finally print our LinkedList.
*/

void setup(){
  LinkedList l = new LinkedList(); //create a new LinkeList
  l.add(new Node_single(0)); //add element 0
  l.add(new Node_single(1)); //add element 1
  l.add(new Node_single(2)); //add element 2
  l.print_list(); //print the list
}

/*=========== LINKED LIST ===========*/
/*--NODE--*/
class Node_single{
 Node_single next; //pointer to next node
 int id; //atribute id used to store an int value

 Node_single(int id){ //constructor to our Node_single class
   this.id = id; //assign the value sent as a parameter to our class atribute
 }
}
/*--END NODE--*/

/*--LIST--*/
class LinkedList{
  Node_single head;
  /*head of our linked list, without it there is no Linked List since we cannot keep track of where the list starts and the list would be lost in memory*/
//ADD
  void add(Node_single n){
   if(head == null){
     head = n;
   }else{
     Node_single temp = head;
     while(temp.next!=null){
       temp = temp.next;
     }
     temp.next = n;
   }
  }
//PRINT
  void print_list(){
    Node_single temp = head;
    while(temp.next!=null){
      print(temp.id+"->");
      temp = temp.next;
    }
    print(temp.id);
    println();
  }
}
/*--END LIST--*/
/*=========== END LINKED LIST ===========*/
