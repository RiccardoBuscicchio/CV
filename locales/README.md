# CV Localization System

This directory contains translation files for generating the CV in different languages.

## Structure

Each language has its own JSON file (e.g., `en.json` for English, `it.json` for Italian).

## Translation File Format

Each translation file contains:
- `language_code`: ISO 639-1 language code (e.g., "en", "it")
- `language_name`: Human-readable language name
- `babel_language`: LaTeX babel package language name (e.g., "english", "italian")
- `sections`: Translations for section headings
- `labels`: Translations for labels and field names (including document titles)
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
4. Update the following fields:
   - `language_code` (e.g., "fr")
   - `language_name` (e.g., "Français")
   - `babel_language` (e.g., "french" - must match a LaTeX babel language)
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

**Important**: The `--lang` parameter localizes the structure files (CV.tex, preamble.tex, publist.tex, talklist.tex) from their `.template` versions, so it must be specified each time you run the script.

## What Gets Localized

The localization system translates:

1. **Document titles**: "Curriculum Vitae", "Publication list", "Presentations"
2. **Section headings**: "Contacts", "Education", "Publications", etc.
3. **Field labels**: "Email", "Address", "Nationality", "Date", etc.
4. **Generated content**: Metrics descriptions, paper lists, talks, supervision notes
5. **LaTeX babel language**: Automatic date formatting and hyphenation rules

## Notes

- LaTeX special characters (like `\`, `{`, `}`) must be properly escaped in the JSON strings
- Some strings contain LaTeX commands for formatting (e.g., `\\textbf{}`, `\\ae`)
- Keep the structure of formatted strings consistent with the English version
- The `babel_language` field must match a valid LaTeX babel language name
