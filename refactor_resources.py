import glob


def rename(resource_map, language="english", section='01-responsive-web-design'):
    """
    Takes in an online resource and replaces all occurrences within a given language and section of the curriculum
    :param resource_map: { original_url: local_resource, ... }
    :param language: language of curriculum
    :param section: section to replace within
    :return:
    """
    dir = '/Users/james/github/FCC/curriculum/challenges/'+language+'/'+section+'/**/*.md'
    for i, pathAndFilename in enumerate(glob.iglob(dir, recursive=True)):
        # title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        with open(pathAndFilename, 'r') as file:
            contents = file.readlines()
            for i, line in enumerate(contents):
                for from_url in resource_map.keys():
                    if from_url in line:
                        print("changed line", i+1)
                        contents[i] = line.replace(from_url, resource_map[from_url])

        with open(pathAndFilename, 'w') as file:
            file.writelines(contents)


def find_resources(language="english", section='01-responsive-web-design'):
    """
    Searches throughout all .md file in curriculum section and find online references
    :param language: The language of the curriculum (english, arabic, chinese, portuguese, russian, spanish)
    :param section: e.g. 01-responsive-web-design
    :return:
    """
    https = []
    dir = '/Users/james/github/FCC/curriculum/challenges/'+language+'/'+section+'/**/*.md'
    for i, pathAndFilename in enumerate(glob.iglob(dir, recursive=True)):
        with open(pathAndFilename, 'r') as file:
            contents = file.readlines()
            for i, line in enumerate(contents):
                if "https://" in line:
                    for word in [x for x in line.split(" ") if "https://" in x]:
                        if word not in https:
                            https.append(word)

    with open("resources.txt", 'w') as file:
        file.writelines(https)


resource_map = {
    'https://bit.ly/fcc-cats': '/fcc-cats.jpg',
    'https://cdn-media-1.freecodecamp.org/imgr/MJAkxbh.png': '/background.png',
    'https://cdn-media-1.freecodecamp.org/imgr/eWWi3gZ.gif': '/offset.gif',
    # 'https://en.wikipedia.org/wiki/Larry_Page': '',
    # 'https://en.wikipedia.org/wiki/Sergey_Brin': '',
    # 'https://freecatphotoapp.com/': '',
    # 'https://en.wikipedia.org/wiki/Color_model': '',
    'https://bit.ly/smallgooglelogo': '/google.png',
    'https://bit.ly/fcc-relaxing-cat': '/relaxing-cat.jpg',
    'https://bit.ly/fcc-lasagna': '/lasagna.jpg',
    # 'https://freecatphotoapp.com/submit-cat-photo': '',
    'https://www.freecodecamp.org': 'https://localhost:8000',
    # 'https://codepen.io': '',
    # 'https://codepen.io/freeCodeCamp/full/VPaoNP': '',
    # 'https://en.wikipedia.org/wiki/User_story': '',
    # 'https://codepen.io/freeCodeCamp/pen/MJjpwO': '',
    'https://cdn.freecodecamp.org/testable-projects-fcc/v1/bundle.js': '/bundle.js',
    # 'https://codepen.io/freeCodeCamp/full/NdrKKL': '',
    # 'https://codepen.io/freeCodeCamp/full/zNqgVx': '',
    # 'https://codepen.io/freeCodeCamp/full/zNBOYG': '',
    # 'https://codepen.io/freeCodeCamp/full/RKRbwL': '',
    # 'https://www.freecodecamp.com/email-submit': '',
    'https://s3.amazonaws.com/freecodecamp/FCCStickers-CamperBot200x200.jpg': '/FCCStickers-CamperBot.jpg',
    'https://s3.amazonaws.com/freecodecamp/FCCStickerPack.jpg': '/FCCStickerPack.jpg',
    # 'https://en.wikipedia.org/wiki/Hexadecimal': '',
    # 'https://en.wikipedia.org/wiki/RGB_color_model': '',
    'https://fonts.googleapis.com/css?family=Lobster': '/Lobster.css',
    # 'https://fonts.google.com/': '',
    'https://s3.amazonaws.com/freecodecamp/screen-reader.mp3': '/screen-reader.mp3',
    'https://tinyurl.com/coffee-beans-fcc': '/coffee-beans.jpeg',
    'https://tinyurl.com/cafe-coffee-fcc': '/cafe-coffee-fcc.jpg',
    'https://tinyurl.com/cafe-pie-fcc': '/cafe-pie-fcc.jpg',
    'https://www.freecatphotoapp.com/your-image.jpg': '/your-image.jpg',
    'https://www.w3.org/TR/css-flexbox-1/images/flex-direction-terms.svg': '/flex-direction-terms.svg',
    'https://freecodecamp.s3.amazonaws.com/quincy-twitter-photo.jpg': '/quincy.jpg',
}

# BE VERY CAREFUL WHEN RUNNING THIS!!!
# rename(resource_map)
