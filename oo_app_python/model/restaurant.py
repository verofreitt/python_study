from model.assessment import Assessment

class Restaurant:
    """Represents a restaurant and its characteristics."""
    restaurants = []

    def __init__(self, name, category):
        """
        Initializes a Restaurant instance.

        Parameters:
        - name (str): The name of the restaurant.
        - category (str): The category of the restauran
        """
        self._name = name.title()
        self._category = category.upper()
        self._ative = False
        self._assessment = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        """Returns a string representation of the restaurant."""
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        """Displays a formatted list of all restaurants."""
        print(f'{"Name restaurant".ljust(25)} | {"Category".ljust(25)} | {"Assessment".ljust(25)} | {"Status"}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_assessment.ljust(25))} | {restaurant.ative}')

    @property
    def ative(self):
        """Returns a symbol indicating the restaurant's activity status."""
        return '☒' if self._ative else '☐'
    
    def alt_status(self):
        """Toggles the activity status of the restaurant."""
        self._ative = not self._ative

    def receiver_assessment(self, client, note):
        """
        Registers a review for the restaurant.

        Parameters:
        - customer (str): The name of the customer who made the review.
        - rating (float): The rating given to the restaurant (between 1 and 5).
        """
        if 0 < note <= 5:
            assessment = Assessment(client, note)
            self._assessment.append(assessment)

    @property
    def average_assessment(self):
        """Calculates and returns the average rating of the restaurant."""
        if not self._assessment:
            return '-'
        note_sum = sum(assessment._note for assessment in self._assessment)
        amount_note = len(self._assessment)
        average = round(note_sum / amount_note, 1)
        return average