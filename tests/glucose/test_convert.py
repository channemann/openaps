from unittest import TestCase

from openaps.glucose.convert import Convert


class ConvertTestCase (TestCase):
    """
        Test a variety of blood glucose values.
        Note that the Glucose converter does *not* (and should not)
        round values. See the glucose.round module for that.
    """

    # The List of mmol/L sugars was generated by a run of
    # random.uniform(0.0,35.0)
    MMOL_LIST = [
        0.10200000000000001, 1.3519999999999999, 1.6260000000000001, 3.811,
        4.333000000000001, 6.683, 8.024, 8.171,
        10.671, 11.062000000000001, 13.943999999999999, 14.902,
        17.683000000000003, 20.474, 24.657, 25.338, 28.008, 33.665,
        34.626000000000005, 34.817]

    # This list needs to match the above MMOL_LIST - it's built mathematically
    # and manually, but has been checked against
    # http://www.diabetes.co.uk/blood-sugar-converter.html
    #
    # Note that the URL above only rounds to one digit
    MGDL_LIST = [
        1.836, 24.336, 29.268, 68.598,
        77.99400000000001, 120.294, 144.432, 147.07799999999997,
        192.07799999999997, 199.116, 250.992, 268.236,
        318.29400000000004, 368.532, 443.826, 456.084, 504.144, 605.97,
        623.268, 626.706]

    def test_mmol_l_to_mg_dl(self):
        results = [Convert.mmol_l_to_mg_dl(mmol) for mmol in
                   self.MMOL_LIST]

        self.assertListEqual(
            results,
            self.MGDL_LIST
        )

    def test_mg_dl_to_mmol_l(self):
        results = [Convert.mg_dl_to_mmol_l(mg_dl) for mg_dl in
                   self.MGDL_LIST]

        self.assertListEqual(
            results,
            self.MMOL_LIST
        )
