from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    """
    Parses a date in the format mm/dd/yyyy and returns a datetime object.
    """
    dt = datetime.strptime(text, "%m/%d/%Y")
    return dt

def formatdate_ymd(date: datetime) -> str:
    """
    Takes a datetime object and returns a string in the format yyyy-mm-dd.
    """
    return date.strftime("%Y-%m-%d")


def test_parsedate_mdy():
    # Test the parsedate_mdy function
    assert parsedate_mdy("12/31/2020") == datetime(2020, 12, 31)
    assert parsedate_mdy("03/06/2020") == datetime(2020, 3, 6)

def test_formatdate_ymd():
    # Test the formatdate_ymd function
    assert formatdate_ymd(datetime(2020, 12, 31)) == "2020-12-31"
    assert formatdate_ymd(datetime(2020, 3, 6)) == "2020-03-06"