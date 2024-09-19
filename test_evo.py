import pytest
from Evo_self import Evo

def test_evo():
    """The Car class takes NO arguments"""
    evo = Evo()
    assert evo.driver is None
    assert evo.distance == 0

def test_evo_no_arguments():
    """The Car class takes NO arguments"""
    with pytest.raises(TypeError):
        Evo(None, 0)

def test_evo_cannot_evo_without_driver():
    """The evo must have a driver before it can be used"""
    evo = Evo()
    with pytest.raises(RuntimeError):
        evo.drive(100)

def test_evo_start_rental():
    """
    When the rental begins, the driver is set.
    There can only be one rental at a time.
    """

    evo = Evo()
    evo.start_rental("Tim")
    assert evo.driver == "Tim"

    with pytest.raises(RuntimeError):
        evo.start_rental("Other driver")

def test_evo_drive():
    """The drive method keeps track of the distance ridden"""
    evo = Evo()
    evo.start_rental("Tim")
    assert evo.distance == 0
    evo.drive(100)
    assert evo.distance == 100
    evo.drive(200)
    assert evo.distance == 300

    with pytest.raises(AttributeError):
        evo.drive(-500)

    assert evo.distance == 300

def test_evo_end_rental():
    """
    end_rental terminates the rental, and RETURNS the distance driven
    driver and distance are reset to their default values (None, 0)
    """

    evo = Evo()
    with pytest.raises(RuntimeError):
        evo.end_rental()

    evo.start_rental("Tim")
    evo.drive(500)
    distance = evo.end_rental()
    assert distance == 500
    assert evo.distance == 500
    assert evo.driver is None

def test_two_rentals():
    evo = Evo()
    evo.start_rental("Tim")
    evo.drive(500)
    tim = evo.end_rental()

    evo.start_rental("Bob")
    evo.drive(100)
    bob = evo.end_rental()

    assert evo.distance == 600
    assert tim == 500
    assert bob == 100