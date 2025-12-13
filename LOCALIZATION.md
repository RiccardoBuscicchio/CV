# CV Localization System

This document describes the localization system for generating the CV in multiple languages.

## Overview

The CV production system now supports multiple languages through a JSON-based localization system. This allows you to generate your CV, publication list, and talk list in different languages.

## Directory Structure

```
locales/
├── README.md          # Detailed instructions for translators
├── en.json            # English translations (default)
├── it.json            # Italian translations
└── [lang].json        # Additional language files
```

## Quick Start

### Using an Existing Language

To generate a CV in a specific language:

```bash
# Generate CV in English (default)
python makeCV.py --connected --token YOUR_ADS_TOKEN

# Generate CV in Italian
python makeCV.py --connected --lang it --token YOUR_ADS_TOKEN

# Generate CV in Italian with short version
python makeCV.py --connected --lang it --token YOUR_ADS_TOKEN
python makeCV.py --short --lang it
```

### Adding a New Language

1. Copy an existing translation file from the `locales/` directory:
   ```bash
   cp locales/en.json locales/fr.json
   ```

2. Edit the new file and translate all strings:
   - Update `language_code` (e.g., "fr" for French)
   - Update `language_name` (e.g., "Français")
   - Translate all text strings while preserving LaTeX formatting

3. Test the new translation:
   ```bash
   python makeCV.py --connected --lang fr --token YOUR_ADS_TOKEN
   ```

## Translation File Structure

Each translation file contains the following sections:

- **sections**: Section headings (Contacts, Education, Publications, etc.)
- **labels**: Field labels (Email, Address, Nationality, etc.)
- **papers**: Publication-related text
- **metrics**: Metrics and statistics text
- **supervision**: Student supervision section text
- **refereeing**: Refereeing section text
- **codes**: Codes and datasets section text
- **talks**: Talks section text

## Important Notes

### LaTeX Special Characters

Translation strings may contain LaTeX commands and special characters. These must be properly escaped in JSON:

- Backslashes: Use `\\` for LaTeX commands (e.g., `"\\textbf{}"`)
- Braces: Use `{` and `}` for LaTeX grouping
- Special characters: Use LaTeX escapes (e.g., `\\ae` for æ, `\\`{a}` for à)

Examples:
```json
"curriculum_vitae": "Curriculum Vit\\ae",
"nationality": "Nazionalit\\`{a}",
"short_author_papers": "short-author papers published in major peer-reviewed journals"
```

### Preserving Formatting

When translating, maintain the same structure and formatting as the English version:

- Keep punctuation consistent (commas, periods, colons)
- Preserve spacing where it matters
- Don't remove LaTeX commands unless you understand their purpose

## Workflow Integration

The localization system integrates with the existing CI/CD workflow. To support multiple languages in CI:

1. Modify `.github/workflows/main.yml` to generate CVs in different languages
2. Add language-specific build steps
3. Deploy multiple language versions

Example workflow modification:
```yaml
- name: Run Python script for Italian
  run: conda run --name buildcv bash -c "python makeCV.py --connected --lang it --token ${{ secrets.ADS_TOKEN }}"
```

## Supported Languages

Currently supported languages:
- **en** - English (default)
- **it** - Italian

## Contributing

To contribute a new language translation:

1. Create a new translation file in `locales/`
2. Follow the structure of existing translation files
3. Test your translation thoroughly
4. Submit a pull request with your translation

## Troubleshooting

### Translation file not found
If you get a warning about a missing translation file, the system will fall back to English. Check that:
- The language code is correct (e.g., "fr" not "FR")
- The translation file exists in the `locales/` directory
- The filename matches the pattern `[lang].json`

### LaTeX compilation errors
If the PDF compilation fails after adding a translation:
- Check for unescaped LaTeX special characters
- Verify all braces are balanced
- Ensure LaTeX commands are properly formatted

### Missing translations
If some text appears in English despite using a different language:
- The translation file may be incomplete
- Copy the missing keys from `en.json` and translate them
- Ensure the JSON structure is valid

## Future Enhancements

Potential improvements to the localization system:
- Support for language-specific date formats
- Automatic translation validation
- Multi-language CV generation in a single run
- Language switcher in the CV itself
