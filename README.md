# Auto-filled cv, publication list, and talk list
![main](https://github.com/RiccardoBuscicchio/CV/actions/workflows/main.yml/badge.svg?branch=main)

Products:
- Latest CV: [view](http://github.com/RiccardoBuscicchio/CV/blob/build/CV.pdf) - [download](http://github.com/RiccardoBuscicchio/CV/raw/build/CV.pdf)
- Latest CV (short version): [view](http://github.com/RiccardoBuscicchio/CV/blob/build/CVshort.pdf) - [download](http://github.com/RiccardoBuscicchio/CV/raw/build/CVshort.pdf)
- Latest publication list: [view](http://github.com/RiccardoBuscicchio/CV/blob/build/publist.pdf) - [download](http://github.com/RiccardoBuscicchio/CV/raw/build/publist.pdf)
- Latest talk list: [view](http://github.com/RiccardoBuscicchio/CV/blob/build/talklist.pdf) - [download](http://github.com/RiccardoBuscicchio/CV/raw/build/talklist.pdf)

## Localization

The CV production system now supports multiple languages! See [LOCALIZATION.md](LOCALIZATION.md) for detailed documentation.

**Quick start:**
```bash
# Generate CV in English (default)
python makeCV.py --connected --token YOUR_ADS_TOKEN

# Generate CV in Italian
python makeCV.py --connected --lang it --token YOUR_ADS_TOKEN
```

**Supported languages:**
- English (en) - default
- Italian (it)

To add a new language, see the [localization documentation](LOCALIZATION.md).

## CI/CD

The continuous integration workflow automatically builds and deploys the CV and related documents on every push to the main branch. The workflow has been optimized with comprehensive caching to significantly reduce build times. See [CI_OPTIMIZATION.md](CI_OPTIMIZATION.md) for details.
