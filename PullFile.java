import java.io.FileNotFoundException;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class PullFile
{
    public static void main(String[] a)
    {
        String username = "batlynx".toLowerCase();
        String content = null;
        URLConnection connection = null;
        try {
            connection =  new URL("https://www.chess.com/awards/" + username + "/achievements").openConnection();
            Scanner scanner = new Scanner(connection.getInputStream());
            scanner.useDelimiter("\\Z");
            content = scanner.next();
            scanner.close();
        }catch ( FileNotFoundException e ) {
            System.out.println("Unable to read achievements. Did you put in the username correctly?");
            return;
        }catch (Exception e ){
            e.printStackTrace();
        }

        int achievementCount = 0;

        // Flag to find achievement element
        String awardIndicator = "awards-page-list-item";

        // Flag to determine if the achievement is still locked
        String lockedIndicator = "data-is-hidden=\"1\"";
        boolean isLocked = false;

        for (int i = 0; i < content.length() - awardIndicator.length(); i++)
        {
            if(content.startsWith(awardIndicator, i))
            {
                // Determine if the achievement is still locked
                for (int j = 0; j < 500; j++)
                {
                    if(content.startsWith(lockedIndicator, (i + j))) {
                        isLocked = true;
                        break;
                    }
                }

                // If the achievement isn't locked, then display the achievement name
                if(!isLocked)
                {
                    System.out.println(findName(content.substring(i, i + 200), "data-code=\"", '\"'));
                    achievementCount++;
                }
                // If the achievement is locked, reset the isLocked variable
                else
                    isLocked = false;

            }
        }
        System.out.println("Achievements: " + achievementCount);
    }

    private static String findName(String section, String before, char after)
    {
        String name = "";

        int i;

        for (i = 0; i < section.length() - before.length(); i++)
        {
            if(section.startsWith(before, i))
            {
                i += before.length();
                break;
            }
        }

        while(section.charAt(i) != after)
        {
            name += section.charAt(i++);
        }

        return name;
    }
}
