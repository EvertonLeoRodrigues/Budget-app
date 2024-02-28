class Category:

    def __init__(self, budget):
        self.budget = budget
        self.ledger = []
        

    def deposit(self, amount, description=""):
        """A deposit method that accepts an amount and description.
        If no description is given, it should default to an empty string. 
        The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
        """
        return self.ledger.append({'amount':amount, 'description': description})

    def withdraw(self, amount, description=""):
        """A withdraw method that is similar to the deposit method, 
        but the amount passed in should be stored in the ledger as a negative number. 
        If there are not enough funds, nothing should be added to the ledger. 
        This method should return True if the withdrawal took place, and False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        
        return False
        

    def get_balance(self):
        """A get_balance method that returns the current balance of the budget 
        category based on the deposits and withdrawals that have occurred.
        """
        return sum(category['amount'] for category in self.ledger)
    

    def transfer(self, amount, category):
        """A transfer method that accepts an amount and another budget category as arguments. 
        The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
        The method should then add a deposit to the other budget category with the amount and 
        the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. 
        This method should return True if the transfer took place, and False otherwise.
        """
        if self.check_funds(amount):
            self.withdraw(amount, description = f'Transfer to {category.budget}')
            category.deposit(amount, description = f'Transfer from {self.budget}')
            return True
        return False
        
        

    def check_funds(self, amount):
        """A check_funds method that accepts an amount as an argument. 
        It returns False if the amount is greater than the balance of the budget category and returns True otherwise. 
        This method should be used by both the withdraw method and transfer method.

        Args:
            amount (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.get_balance() >= amount
        

    def __str__(self):
        """*************Food*************
            initial deposit        1000.00
            groceries               -10.15
            restaurant and more foo -15.89
            Transfer to Clothing    -50.00
            Total: 923.96
            ***********Clothing***********
            Transfer from Food       50.00
                                    -25.55
        """
        title = f'{self.budget:*^30}\n'
        items = ''
        for item in self.ledger:
            items+=f'{item['description'][:23]:23}{item['amount']:7.2f}\n'
        total = f'Total: {self.get_balance():.2f}'
        
        return title + items + total
        
        


def create_spend_chart(categories):
    """Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. 
    It should return a string that is a bar chart.

    The chart should show the percentage spent in each category passed in to the function. 
    The percentage spent should be calculated only with withdrawals and not with deposits. 
    Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. 
    The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. 
    Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

    This function will be tested with up to four categories.

    Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

    Args:
        categories (list): List of categories
    """
    total_spent_category = [(sum(item['amount'] for item in category.ledger if item['amount']<0)) for category in categories]
    
    total_spent = sum(total_spent_category)
    
    
    percentages = [int((spent_category/total_spent)*100) for spent_category in total_spent_category]
    
    chart = 'Percentage spent by category\n'
    
    for i in range(100, -1, -10):
        chart += f'{i:3}|'
        for p in percentages:
            if p >= i:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'
        
    
    chart += '    ' + '---'*len(categories) + '-\n'
    
    max_name_length = max([len(category.budget) for category in categories])
    for i in range(max_name_length):
        chart += '     '
        for category in categories:
            if i < len(category.budget):
                chart += f'{category.budget[i]}  '
            else:
                chart += '   '
        
        if i < (max_name_length-1):         
            chart += '\n'
        
    
        
    return chart
    
        




            
        





