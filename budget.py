class Category:
    def __init__(self,category):
        self.category= category
        self.ledger=[] 
    
    def deposit(self,amount,description=''):
        if (type(amount) != int or type(amount) != float) and amount<0:
            raise Exception(f"Error: amount to deposit in {self.category} category balance has to be a positive number")
        self.ledger.append({'amount': amount,'description': description})
    
    def withdraw(self,amount,description=''):
        if type(amount) != int and type(amount) != float:
            raise Exception(f"Error: amount to withdraw from {self.category} category balance has to be a negative number")
        if not self.check_funds(amount):
            return False
        if amount>0:
           amount*=-1
        self.ledger.append({'amount': amount,'description': description})
        return True
    
    def get_balance(self):
        balance=0
        for action in self.ledger:
            balance+=action['amount']
        return balance
    
    def transfer(self,amount,target):
        if (type(amount) != int and type(amount) != float):
            raise Exception(f"Error: amount to transfer from {self.category} category balance has to be a number")
        if not isinstance(target,Category):
            raise Exception("Error: Category does not exist")
        enoughFundsToTransfer=self.withdraw(amount,f"Transfer to {target.category}")
        if not enoughFundsToTransfer:
            return False
        target.deposit(amount,f"Transfer from {self.category}")
        return True
    
    def check_funds(self,amount):
        if abs(amount)>self.get_balance():
            # Not enough funds to withdraw
            return False
        return True
    # Category String output
    def __str__(self):
        #Arrange category's name with *. Max 30 char.
        header=self.category.center(30,'*')
        body=''
        #Loop thro ledger ang get every action, then arrange description (max 23)+ amount fixed to max 2 decimals(max 7) in a string.
        for action in self.ledger:
            description=action['description'][0:23]
            description=description.ljust(23)
            amount=round(action['amount'],2)
            if type(amount) == int:
                amount=str(amount)+'.00'
            amount=str(amount).rjust(7)
            body+=description+amount+'\n'
        #Line displays category's total.
        footer='Total: '+str(self.get_balance())
        return f"{header}\n{body}{footer}"
    
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if type(value) != str:
            raise "Error: category's name is not a String"
        self._category=value

def create_spend_chart(categories):
    
    expensesList=[]
    totalSpent=0
    # make total expenses list by category
    for category in categories:
        expense={'name': category.category,'total-spent':0}
        for action in category.ledger:
            if action['amount']<0:
                expense['total-spent']+=abs(action['amount'])
        expensesList.append(expense)
    # calculate overall total spent
    for category in expensesList:
        totalSpent+=category['total-spent']
    
    output='Percentage spent by category\n'
    tickNum=100
    
    while(tickNum >=0):
        segment=(str(tickNum)+'|').rjust(4)
        threshold=tickNum-5
        for category in expensesList:
            percentageSpent=round((category['total-spent']/totalSpent)*100)
            if percentageSpent>threshold:
                segment+=' o '
            else:
                segment+='   '
        output+=segment+' \n'
        tickNum-=10
    
    output+='    '+'-'*(len(expensesList)*3+1)+'\n'
    # Determine highest category name string
    strLen=0
    for category in expensesList:
        if len(category['name'])>strLen:
            strLen=len(category['name'])
    #arrange characters below bar chart
    for i in range(0,strLen):
        row='    '
        for category in expensesList:
            name=category['name']
            if i>=len(name):
                row+='   '
            else:
                row+=name[i].center(3)
        row+=' '
        if i<strLen-1:
            row+='\n'
        output+=row
    
    return output