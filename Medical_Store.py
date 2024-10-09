{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNAt3i7dZK/0Q7N5unhkh+r",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aartit1234/aartit1234/blob/main/Medical_Store.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Medical store management system**"
      ],
      "metadata": {
        "id": "7PykPyysNEMA"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Code for the Admin main module in the Medical Store Management System Project in Python"
      ],
      "metadata": {
        "id": "lhohp3NRPO-S"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def open_win(): #OPENS MAIN MENU---------\n",
        "    global apt, flag\n",
        "    flag='apt'\n",
        "    apt=Tk()\n",
        "    apt.title(\"Interface\")\n",
        "    Label(apt, text=\"EVANZ MEDICAL STORE COMPANY\").grid(row=0,column=0,columnspan=3)\n",
        "    Label(apt, text='*'*80).grid(row=1,column=0,columnspan=3)\n",
        "    Label(apt, text='-'*80).grid(row=3,column=0,columnspan=3)\n",
        "\n",
        "    Label(apt, text=\"Stock Maintenance\",  bg='green', fg='white').grid(row=2,column=0)\n",
        "    Button(apt,text='New V.C.', width=25, bg='green', fg='white', command=val_cus).grid(row=4,column=0)\n",
        "    Button(apt,text='Add product to Stock', bg='green', fg='white', width=25,command=stock).grid(row=5,column=0)\n",
        "    Button(apt,text='Delete product from Stock', bg='red', fg='white', width=25, command=delete_stock).grid(row=6,column=0)\n",
        "\n",
        "\n",
        "    Label(apt, text=\"Access Database\",  bg='blue', fg='white').grid(row=2,column=1)\n",
        "    Button(apt,text='Modify',width=15,  bg='blue', fg='white', command=modify).grid(row=4,column=1)\n",
        "    Button(apt,text='Search', width=15,  bg='blue', fg='white', command=search).grid(row=5,column=1)\n",
        "    Button(apt,text='Expiry Check',  bg='red', fg='white', width=15, command=exp_date).grid(row=6,column=1)\n",
        "\n",
        "    Label(apt, text=\"Handle Cash Flows\", bg='skyblue', fg='black').grid(row=2,column=2)\n",
        "    Button(apt,text=\"Check Today's Revenue\", bg='skyblue', fg='black', width=20,command=show_rev).grid(row=5,column=2)\n",
        "    Button(apt,text='Billing', width=20, bg='skyblue', fg='black', command=billing).grid(row=4,column=2)\n",
        "    Button(apt,text='Logout', bg='red', fg='white', width=20, command=again).grid(row=6, column=2)\n",
        "    apt.mainloop()"
      ],
      "metadata": {
        "id": "hmU5MtNOSkXE"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Code for the add customer in Medical Store Management System Project in Python."
      ],
      "metadata": {
        "id": "DEQ0385bPduM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def val_cus():  #to enter NEW VALUED CUSTOMER------------\n",
        "    global val, flag, dbt, name_vc, add_vc, cur, c, vc_id\n",
        "    apt.destroy()\n",
        "    cur.execute(\"select * from cus\")\n",
        "    flag='val'\n",
        "    val=Tk()\n",
        "    Label(val, bg='blue', fg='white',text=\"*ENTER VALUED CUSTOMER DETAILS*\").grid(row=0,column=0,columnspan=3)\n",
        "    Label(val,text=\"-\"*60).grid(row=1,column=0,columnspan=3)\n",
        "    Label(val,text=\"Name: \").grid(row=2,column=0)\n",
        "    name_vc=Entry(val)\n",
        "    name_vc.grid(row=2, column=1)\n",
        "    Label(val,text=\"Address: \").grid(row=3,column=0)\n",
        "    add_vc=Entry(val)\n",
        "    add_vc.grid(row=3, column=1)\n",
        "    Label(val,text=\"Value Id: \").grid(row=4,column=0)\n",
        "    vc_id=Entry(val)\n",
        "    vc_id.grid(row=4, column=1)\n",
        "    Button(val,text='Submit',bg='blue', fg='white',command=val_get).grid(row=5, column=1)\n",
        "    Button(val,text='Main Menu', bg='green', fg='white',command=main_menu).grid(row=5, column=2)\n",
        "    Label(val,text='-'*60).grid(row=6,column=0,columnspan=3)\n",
        "    val.mainloop()"
      ],
      "metadata": {
        "id": "agIR9IdRPfLY"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Code for the add product in the Medical Store Management System Project in Python."
      ],
      "metadata": {
        "id": "9GACVcAoP2BV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def stock():    #add to stock window-------------------ADD TO STOCK\n",
        "    global cur, c, columns, accept, flag, sto, apt\n",
        "    apt.destroy()\n",
        "    flag='sto'\n",
        "    accept=['']*10\n",
        "    sto=Tk()\n",
        "    sto.title('STOCK ENTRY')\n",
        "    Label(sto,text='ENTER NEW PRODUCT DATA TO THE STOCK').grid(row=0,column=0,columnspan=2)\n",
        "    Label(sto,text='-'*50).grid(row=1,column=0,columnspan=2)\n",
        "    for i in range(1,len(columns)):\n",
        "        Label(sto,width=15,text=' '*(14-len(str(columns[i])))+str(columns[i])+':').grid(row=i+2,column=0)\n",
        "        accept[i]=Entry(sto)\n",
        "        accept[i].grid(row=i+2, column=1)\n",
        "    Button(sto,width=15,text='Submit', bg='blue', fg='white',command=submit).grid(row=12,column=1)\n",
        "    Label(sto,text='-'*165).grid(row=13,column=0,columnspan=7)\n",
        "    Button(sto,width=15,text='Reset', bg='red', fg='white',command=reset).grid(row=12,column=0)\n",
        "    Button(sto,width=15,text='Refresh stock',bg='skyblue', fg='black',command=ref).grid(row=12,column=4)\n",
        "    for i in range(1,6):\n",
        "        Label(sto,text=columns[i]).grid(row=14,column=i-1)\n",
        "    Label(sto,text='Exp           Rack   Manufacturer                      ').grid(row=14,column=5)\n",
        "    Button(sto,width=10,text='Main Menu', bg='green', fg='white',command=main_menu).grid(row=12,column=5)\n",
        "    ref()\n",
        "    sto.mainloop()"
      ],
      "metadata": {
        "id": "-OZbF2rCP7U1"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Code for the deleted product in the Medical Store Management System Project in Python"
      ],
      "metadata": {
        "id": "Ahn5A52AP-1t"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def delete_stock(): #OPENS DELETE WINDOW--------------DELETES A PARTICULAR STOCK ITEM\n",
        "    global cur, c, flag, lb1, d\n",
        "    apt.destroy()\n",
        "    flag='d'\n",
        "    d=Tk()\n",
        "    d.title(\"Delete a product from Stock\")\n",
        "    Label(d,text='Enter Product to delete:').grid(row=0,column=0)\n",
        "    Label(d,text='',width=30,bg='white').grid(row=0,column=1)\n",
        "    Label(d,text='Product').grid(row=2,column=0)\n",
        "    Label(d,text='Qty.  Exp.dt.     Cost                           ').grid(row=2,column=1)\n",
        "    ren()\n",
        "    b=Button(d,width=20,text='Delete', bg='red', fg='white',command=delt).grid(row=0,column=3)\n",
        "    b=Button(d,width=20,text='Main Menu', bg='green', fg='white',command=main_menu).grid(row=5,column=3)\n",
        "    d.mainloop()"
      ],
      "metadata": {
        "id": "zL3W_FLqQBze"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Code for checking expired medicine in Medical Store Management System Project in Python."
      ],
      "metadata": {
        "id": "vUpDuO0kQIK2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def exp_date(): # expiry window open-------------------EXPIRY\n",
        "    global exp, s,c, cur, flag, apt, flags\n",
        "    apt.destroy()\n",
        "    flag='exp'\n",
        "    from datetime import date\n",
        "    now=time.localtime()\n",
        "    n=[]\n",
        "    cur.execute(\"select *from med\")\n",
        "    for i in cur:\n",
        "        n.append(i[1])\n",
        "    c.commit()\n",
        "    exp=Tk()\n",
        "    exp.title('EXPIRY CHECK')\n",
        "    Label(exp,text='Today : '+str(now[2])+'/'+str(now[1])+'/'+str(now[0])).grid(row=0, column=0, columnspan=3)\n",
        "    Label(exp,text='Selling Expired Medicines and Drugs is Illegal').grid(row=1, column=0,columnspan=3)\n",
        "    Label(exp,text='-'*80).grid(row=2, column=0,columnspan=3)\n",
        "    s=Spinbox(exp,values=n)\n",
        "    s.grid(row=3, column=0)\n",
        "    Button(exp,text='Check Expiry date', bg='red', fg='white', command=s_exp).grid(row=3, column=1)\n",
        "    Label(exp,text='-'*80).grid(row=4, column=0,columnspan=3)\n",
        "    if flags=='apt1':\n",
        "        Button(exp,text='Main Menu', bg='green', fg='white', command=main_cus).grid(row=5, column=2)\n",
        "    else:\n",
        "        Button(exp,width=20,text='Check Products expiring', bg='red', fg='white', command=exp_dt).grid(row=5, column=0)\n",
        "        Button(exp,text='Main Menu', bg='green', fg='white', command=main_menu).grid(row=5, column=2)\n",
        "    exp.mainloop()"
      ],
      "metadata": {
        "id": "6G5Rg4yAQL-o"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Code for the Revenue in Medical Store Management System Project in Python"
      ],
      "metadata": {
        "id": "6hS1cW3hQk53"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def show_rev(): # opens revenue window-------------------------TOTAL REVENUE\n",
        "    global c, cur, flag,rev\n",
        "    apt.destroy()\n",
        "    cb=('cus_name','cus_add','items','Total_cost','bill_dt','bill_no','bill','val_id')\n",
        "    flag='rev'\n",
        "    rev=Tk()\n",
        "    total=0.0\n",
        "    today=str(time.localtime()[2])+'/'+str(time.localtime()[1])+'/'+str(time.localtime()[0])\n",
        "    Label(rev,text='Today: '+today).grid(row=0,column=0)\n",
        "    cur.execute('select * from bills')\n",
        "    for i in cur:\n",
        "        if i[4]==today:\n",
        "            total+=float(i[3])\n",
        "    print (total)\n",
        "    Label(rev,width=22,text='Total revenue: PHP '+str(total), bg='blue',fg='white').grid(row=1,column=0)\n",
        "    cx=0\n",
        "    vsb=Scrollbar(orient='vertical')\n",
        "    lb1=Listbox(rev,width=25, yscrollcommand=vsb.set)\n",
        "    vsb.grid(row=2,column=1,sticky=N+S)\n",
        "    lb1.grid(row=2,column=0)\n",
        "    vsb.config( command = lb1.yview )\n",
        "    cur.execute(\"select * from bills\")\n",
        "    for i in cur:\n",
        "      if i[4]==today:\n",
        "        cx+=1\n",
        "        lb1.insert(cx,'Bill No.: '+str(i[5])+'    : PHP '+str(i[3]))\n",
        "    c.commit()\n",
        "    Button(rev,text='Main Menu',bg='green', fg='white',command=main_menu).grid(row=15,column=0)\n",
        "    rev.mainloop()"
      ],
      "metadata": {
        "id": "D22Ws99hQrZB"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Code for the billing in the Medical Store Management System Project in Python."
      ],
      "metadata": {
        "id": "99CUVPbIQ9UH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def billing(): # to create bills for customer------------------BILLING system\n",
        "    global c, cur, apt, flag, t, name, name1, add, st, names, qty, sl, qtys, vc_id, n, namee, lb1\n",
        "    t=0\n",
        "    vc_id=''\n",
        "    names=[]\n",
        "    qty=[]\n",
        "    sl=[]\n",
        "    n=[]\n",
        "    qtys=['']*10\n",
        "    cur.execute(\"select *from med\")\n",
        "    for i in cur:\n",
        "        n.append(i[1])\n",
        "    c.commit()\n",
        "    if flag=='st':\n",
        "        st.destroy()\n",
        "    else:\n",
        "        apt.destroy()\n",
        "    flag='st'\n",
        "    st=Tk()\n",
        "    st.title('BILLING SYSTEM')\n",
        "    Label(st,text='-'*48+'BILLING SYSTEM'+'-'*49).grid(row=0,column=0,columnspan=7)\n",
        "    Label(st,text='Enter Name: ').grid(row=1,column=0)\n",
        "    name1=Entry(st)\n",
        "    name1.grid(row=1, column=1)\n",
        "    Label(st,text='Enter Address: ').grid(row=2,column=0)\n",
        "    add=Entry(st)\n",
        "    add.grid(row=2, column=1)\n",
        "    Label(st,text=\"Value Id (if available)\").grid(row=3, column=0)\n",
        "    vc_id=Entry(st)\n",
        "    vc_id.grid(row=3, column=1)\n",
        "    Button(st,text='Check V.C.', bg='green', fg='white', command=blue).grid(row=4, column=0)\n",
        "    Label(st,text='-'*115).grid(row=6, column=0,columnspan=7)\n",
        "    Label(st,text='SELECT PRODUCT',width=25,relief='ridge').grid(row=7, column=0)\n",
        "    Label(st,text=' RACK  QTY LEFT     COST          ',width=25,relief='ridge').grid(row=7, column=1)\n",
        "    Button(st,text='Add to bill', bg='blue', fg='white', width=15,command=append2bill).grid(row=8, column=6)\n",
        "    Label(st,text='QUANTITY',width=20,relief='ridge').grid(row=7, column=5)\n",
        "    qtys=Entry(st)\n",
        "    qtys.grid(row=8,column=5)\n",
        "    refresh()\n",
        "    Button(st,width=15,text='Main Menu', bg='green', fg='white', command=main_menu).grid(row=1,column=6)\n",
        "    Button(st,width=15,text='Refresh Stock',bg='skyblue', fg='black', command=refresh).grid(row=3,column=6)\n",
        "    Button(st,width=15,text='Reset Bill', bg='red', fg='white', command=billing).grid(row=4,column=6)\n",
        "    Button(st,width=15,text='Print Bill', bg='orange', fg='white', command=print_bill).grid(row=5,column=6)\n",
        "    Button(st,width=15,text='Save Bill', bg='blue', fg='white', command=make_bill).grid(row=7,column=6)\n",
        "\n",
        "    st.mainloop()"
      ],
      "metadata": {
        "id": "tEqPJLhZRAl3"
      },
      "execution_count": 18,
      "outputs": []
    }
  ]
}