from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'prudence'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='1. How old are you?')
    gender = models.StringField(
        choices=['Male', 'Female', 'Other'],
        label='2. What is your gender?',
        widget=widgets.RadioSelect,
    )
    ethnicity = models.StringField(
        choices=['Black African', 'Colored', 'Indian/Asian', 'White'],
        label='3. What is your enthnicity?',
        widget=widgets.RadioSelect,
    )

    Mother_tongue = models.StringField(label='4. What is your mother tongue (language)?')

    Highest_education = models.StringField(
        choices=['No formal education', 'Below matric', 'Matric', 'University education',
                 'Post-graduate studies', 'Prefer not to say'],
        label='5. What is your Highest education?',
        widget=widgets.RadioSelect,
    )
    Employment_status = models.StringField(
        choices=['Permanently employed', 'Contract', 'Unemployed', 'Self-employed',
                 'Prefer not to say'],
        label='6. What is your employment status? ',
        widget=widgets.RadioSelect,
    )
    Housed_income_source = models.StringField(
        choices=['Salaries/Wages', 'Social grants', 'Pension', 'Remittances',
                 'Business income', 'Farming/Agricultural activities', 'Other'],
        label='7. What is your household’s main source of income?',
        widget=widgets.RadioSelect,
    )
    Housed_Total_monthly_income = models.StringField(
        choices=['Less than R 500', 'Between R 500 and R 1000', 'Between R 1000 and R 3000',
                 'Between R 3000 and R 5000',
                 'More than R5000', 'Prefer not to answer'],
        label='8. What is your household’s total monthly income?',
        widget=widgets.RadioSelect,
    )
    crt_bat = models.IntegerField(
        label='''
            A bat and a ball cost 22 dollars in total.
            The bat costs 20 dollars more than the ball.
            How many dollars does the ball cost?'''
    )
    Marital_status = models.StringField(
        choices=['Single', 'Cohabitant', 'Married', 'Separated', 'Divorced', 'Widowed', 'I prefer not to answer'],
        label='9. What is your marital status? ',
        widget=widgets.RadioSelect,
    )
    Relationship_to_the_head = models.StringField(
        choices=['Self', 'Spouse', 'Child', 'Parent', 'Sibling', 'I do not know', 'I prefer not to answer'],
        label='10. What is your relationship to the head of the household? ',
        widget=widgets.RadioSelect,
    )
    Residence_type = models.StringField(
        choices=['Rented rooms', 'Squatter camp', 'Reconstruction and Development Programme (RDP) Houses',
                 'Rented flat or house', 'Own a house or flat', 'I do not know', 'I prefer not to answer'],
        label='11. Do you or your household live in a ',
        widget=widgets.RadioSelect,
    )
    Access_to_a_bank_account = models.StringField(
        choices=['Yes', 'No'],
        label='12. Do you have access to a bank account? ',
        widget=widgets.RadioSelect,
    )
    crt_widget = models.IntegerField(
        label='''
            "If it takes 5 machines 5 minutes to make 5 widgets,
            how many minutes would it take 100 machines to make 100 widgets?"
            '''
    )
    Income_earnings = models.StringField(
        choices=['Place of employment', 'Scholarships', 'Parents', 'Government grant', 'Business income', 'Other'],
        label='13.How do you earn your income?',
        widget=widgets.RadioSelect,
    )
    Insurance_policy = models.StringField(
        choices=['Yes', 'No'],
        label='14. Do you have an insurance policy?',
        widget=widgets.RadioSelect,
    )
    Type_of_insurance_policy = models.StringField(
        choices=['Life insurance policy', 'Education insurance policy', 'Theft insurance policy',
                 'Car and House insurance policy', 'Stokvel', 'Hospital insurance policy', 'Other'],
        label='15. What type of insurance policy do you have? Select 1 option from below and provide the next on the following question if you have any?',
        widget=widgets.RadioSelect,
    )
    Other_insurance_policy = models.StringField(
        label='16. Please provide other insurance policy you might have, other than the insurance policy you have chosen above in Question 15?')

    Do_you_save = models.StringField(
        choices=['Yes', 'No'],
        label='17. Do you save?',
        widget=widgets.RadioSelect,
    )
    Savings_percentage = models.StringField(
        choices=['0%', '1-25%', '26-50%', '51-75%', '76-100%'],
        label='18. What are your savings as a percentage of your income percentage?',
        widget=widgets.RadioSelect,
    )
    Reason_for_saving = models.StringField(
        choices=['Retirement', 'Education', 'Purchase of an asset', 'To go on a holiday', 'Payoff debt'],
        label='19. What are your reasons for saving your income?',
        widget=widgets.RadioSelect,
    )
    Other_reasons_for_saving = models.StringField(
        label='20. Please provide other reasons for saving you might have, other than the above you have chosen in Question 19?')

    Reason_for_not_saving = models.StringField(
        choices=['The income you receive is not enough?', 'Have to pay off debt?',
                 'Have to take care of children or elderly persons?'],
        label='21. If you do not save, what might be the reason?',
        widget=widgets.RadioSelect,
    )
    Other_reasons_for_not_saving = models.StringField(
        label='22. Please provide other reasons for not saving, other than the above you have chosen in Question 21?')

    Monthly_budget = models.StringField(
        choices=['Yes', 'No'],
        label='23. Do you create a monthly budget?',
        widget=widgets.RadioSelect,
    )
    Reason_for_purchasing_an_item = models.StringField(
        choices=['Yes, I buy it because of the price', 'No, I do not buy it because of its price',
                 'Yes, I buy it because of the value', 'No, I do not buy it because of its value'],
        label='24. When purchasing an item, do you buy it because of the price or the value you receive from buying it?',
        widget=widgets.RadioSelect,
    )
    Automated_monthly_transfer = models.StringField(
        choices=['Yes', 'No'],
        label='25. Do you have an automated monthly transfer to a dedicated savings/contingency account?',
        widget=widgets.RadioSelect,
    )
    Price_and_product_comparison = models.StringField(
        choices=['Yes', 'No'],
        label='26. Do you compare products and prices from different shops?',
        widget=widgets.RadioSelect,
    )
    Monthly_payments = models.StringField(
        choices=['Yes', 'No'],
        label='27. Do you sometimes miss monthly credit payments?',
        widget=widgets.RadioSelect,
    )
    Budget = models.StringField(
        choices=['Monthly basis?', 'Short-term basis?', 'Long-term basis?'],
        label='28. Do you budget on a...?',
        widget=widgets.RadioSelect,
    )
    Advantages_of_discounts = models.StringField(
        choices=['Yes', 'No'],
        label='29. Do you take advantages of festive offers/seasonal discounts?',
        widget=widgets.RadioSelect,
    )
    Maintenance = models.StringField(
        choices=['Yes', 'No'],
        label='30. Do you undertake periodic maintenance of assets you might own to avoid higher bills at a later stage?',
        widget=widgets.RadioSelect,
    )
    get_1 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )

    get_2 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )

    get_3 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )

    get_4 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )

    get_5 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_6 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'ethnicity', 'Mother_tongue', 'Highest_education', 'Employment_status',
                   'Housed_income_source', 'Housed_Total_monthly_income', 'Marital_status', 'Relationship_to_the_head',
                   'Residence_type', 'Access_to_a_bank_account', 'Income_earnings', 'Insurance_policy',
                   'Type_of_insurance_policy', 'Other_insurance_policy',
                   'Do_you_save', 'Savings_percentage', 'Reason_for_saving', 'Other_reasons_for_saving',
                   'Reason_for_not_saving',
                   'Other_reasons_for_not_saving', 'Monthly_budget', 'Reason_for_purchasing_an_item',
                   'Automated_monthly_transfer', 'Price_and_product_comparison', 'Monthly_payments',
                   'Budget', 'Advantages_of_discounts', 'Maintenance']

class Page1C(Page):
    pass


class Lottery(Page):
    form_model = 'player'
    form_fields = ["get_1", "get_2", "get_3", "get_4", "get_5", "get_6"]

page_sequence = [Demographics, Page1C, Lottery]

