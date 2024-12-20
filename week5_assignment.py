from abc import ABC, abstractmethod
from typing import List
import random

class Superhero(ABC):
    """Abstract base class for all superheroes"""
    
    def __init__(self, name: str, secret_identity: str, power_level: int = 100):
        self._name = name  # Protected attribute
        self.__secret_identity = secret_identity  # Private attribute
        self._power_level = max(0, min(power_level, 100))  # Constrain between 0-100
        self._health = 100
        self._experience = 0
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def power_level(self) -> int:
        return self._power_level
    
    def reveal_identity(self, clearance_level: int) -> str:
        """Only reveal secret identity if proper clearance is provided"""
        if clearance_level >= 5:
            return self.__secret_identity
        return "Access Denied: Insufficient Clearance"
    
    @abstractmethod
    def move(self) -> str:
        """Each hero type must implement their own movement method"""
        pass
    
    @abstractmethod
    def special_ability(self) -> str:
        """Each hero type must implement their unique ability"""
        pass
    
    def gain_experience(self, amount: int) -> None:
        """Gain experience and potentially level up"""
        self._experience += amount
        if self._experience >= 100:
            self._power_level = min(100, self._power_level + 10)
            self._experience = 0
            print(f"{self.name} has leveled up! New power level: {self.power_level}")

class FlyingHero(Superhero):
    """Heroes that can fly"""
    
    def __init__(self, name: str, secret_identity: str, flight_speed: int):
        super().__init__(name, secret_identity)
        self.flight_speed = flight_speed
        self._wings_deployed = False
    
    def move(self) -> str:
        return f"{self.name} soars through the sky at {self.flight_speed} mph!"
    
    def special_ability(self) -> str:
        self._wings_deployed = not self._wings_deployed
        status = "deployed" if self._wings_deployed else "retracted"
        return f"{self.name}'s wings are now {status}!"
    
    def aerial_maneuver(self) -> str:
        """Method specific to flying heroes"""
        maneuvers = ["barrel roll", "loop-de-loop", "steep dive", "vertical climb"]
        return f"{self.name} performs a {random.choice(maneuvers)}!"

class SpeedHero(Superhero):
    """Heroes with super speed"""
    
    def __init__(self, name: str, secret_identity: str, max_speed: int):
        super().__init__(name, secret_identity)
        self.max_speed = max_speed
        self._is_sprinting = False
    
    def move(self) -> str:
        return f"{self.name} races across the ground at {self.max_speed} mph!"
    
    def special_ability(self) -> str:
        self._is_sprinting = not self._is_sprinting
        mode = "Sprint mode" if self._is_sprinting else "Normal mode"
        return f"{self.name} switches to {mode}!"
    
    def time_warp(self) -> str:
        """Method specific to speed heroes"""
        return f"{self.name} moves so fast that time appears to slow down!"

# Example usage and testing
def hero_demonstration():
    # Create instances of different hero types
    swift = SpeedHero("Swift", "Barry Williams", 500)
    eagle = FlyingHero("Eagle Eye", "Sarah Hawks", 200)
    
    # Store heroes in a list to demonstrate polymorphism
    heroes: List[Superhero] = [swift, eagle]
    
    print("=== Hero Movement Demonstration ===")
    for hero in heroes:
        print(hero.move())
        print(hero.special_ability())
        
    print("\n=== Special Abilities ===")
    print(swift.time_warp())
    print(eagle.aerial_maneuver())
    
    print("\n=== Security Test ===")
    print(f"Clearance 1: {swift.reveal_identity(1)}")
    print(f"Clearance 5: {swift.reveal_identity(5)}")
    
    print("\n=== Experience System ===")
    swift.gain_experience(50)
    print(f"{swift.name} XP gained!")
    swift.gain_experience(60)
    print(f"{swift.name} power level: {swift.power_level}")

if __name__ == "__main__":
    hero_demonstration()
