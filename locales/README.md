# CV Localization System

This directory contains translation files for generating the CV in different languages.

## Structure

Each language has its own JSON file (e.g., `en.json` for English, `it.json` for Italian).

## Translation File Format

Each translation file contains:
- `language_code`: ISO 639-1 language code (e.g., "en", "it")
- `language_name`: Human-readable language name
- `sections`: Translations for section headings
- `labels`: Translations for labels and field names
- `papers`: Translations for publication-related text
- `metrics`: Translations for metrics and statistics
- `supervision`: Translations for supervision section
- `refereeing`: Translations for refereeing section
- `codes`: Translations for codes and datasets section
- `talks`: Translations for talks section

## Adding a New Language

1. Copy an existing translation file (e.g., `en.json`)
2. Rename it with the appropriate language code (e.g., `fr.json` for French)
3. Translate all strings in the file
4. Update the `language_code` and `language_name` fields
5. Use the `--lang` option when running `makeCV.py`:
   ```bash
   python makeCV.py --lang fr
   ```

## Usage

To generate a CV in a specific language:
```bash
python makeCV.py --connected --lang it --token YOUR_ADS_TOKEN
```

If no language is specified, English (`en`) is used by default.

## Notes

- LaTeX special characters (like `\`, `{`, `}`) must be properly escaped in the JSON strings
- Some strings contain LaTeX commands for formatting (e.g., `\\textbf{}`, `\\ae`)
- Keep the structure of formatted strings consistent with the English version
