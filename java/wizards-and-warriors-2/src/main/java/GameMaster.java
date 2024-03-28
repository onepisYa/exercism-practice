import java.text.MessageFormat;

public class GameMaster {

    public String describe(Character character){
        return MessageFormat.format("You''re a level {0} {1} with {2} hit points.", String.valueOf(character.getLevel()), character.getCharacterClass(), String.valueOf(character.getHitPoints()));
    }
    public String describe(Destination destination){
        return MessageFormat.format("You''ve arrived at {0}, which has {1} inhabitants.", destination.getName(), String.valueOf(destination.getInhabitants()));
    }

    public String describe(TravelMethod travelMethod){
        String baseString = "You're traveling to your destination ";
        String walking = "by walking.";
        String horseback = "on horseback.";
        switch (travelMethod){
            case WALKING:
                return baseString + walking;
            case HORSEBACK:
                return baseString + horseback;
            default:
                throw new IllegalArgumentException("Travel method not recognized") ;
        }
    }

    public String describe(Character character, Destination destination, TravelMethod travelMethod){
        return MessageFormat.format("{0} {1} {2}", describe(character),  describe(travelMethod), describe(destination));
    }

    public String describe(Character character, Destination destination){
        return MessageFormat.format("{0} {1} {2}", describe(character), describe(TravelMethod.WALKING), describe(destination));
    }
}
