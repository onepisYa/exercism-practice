
# in MacOS

command-line install exercism 


```zsh
brew update
brew install exercism
```

more information at [cli-walkthrough](https://exercism.org/cli-walkthrough)

# first step

To get started, you need to configure the tool with your API token.

Find your token at [settings](https://exercism.io/my/settings)

- [exercism api_cli](https://exercism.org/settings/api_cli)

Then run the configure command:

```zsh
exercism configure --token=YOUR_TOKEN
```

You will see output like this:

```zsh

You have configured the Exercism command-line client:

Config dir:                       /Users/onepisya/.config/exercism
Token:         (-t, --token)      Your Token
Workspace:     (-w, --workspace)  Your Workspace
API Base URL:  (-a, --api)        https://api.exercism.io/v1
```


# example download track

download the track

```zsh
exercism download --track=java --exercise=hello-world

```

more information at [java](https://exercism.org/tracks/java)


# wirte your solution

completely write your solution

then run the test command

for example: java gradlew test

```zsh
 sh ./gradlew test
```

# submit your solution

```zsh
exercism submit /path/to/your/java/your-project/src/main/java/your-project.java
```

# delete build file

example delete java build file

```zsh
rm -rf /path/to/your/java/your-project build and .gradle folder
```

```zsh
rm -rf ./java/**/build ./java/**/.gradle
```


