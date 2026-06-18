# iOS Factory Pipeline

## Phase Map

| Phase | Goal | Output |
| --- | --- | --- |
| Keyword | Pick a winnable search phrase | `aso/keywords.md` |
| Scaffold | Generate or adapt the native app | Xcode project / Swift package |
| Core loop | Deliver one real user outcome | working feature screen |
| Monetize | Add StoreKit/IAP or choose free v1 | product checklist |
| Visuals | Icon, palette, visual direction | `assets/` |
| Screens | Capture and frame App Store screenshots | PNGs by device |
| ASO | Name, subtitle, keywords, description | metadata files |
| Legal | Privacy, terms, age, export compliance | legal docs |
| Grade | Implementation + ASO scorecard | pass/block verdict |
| Release | Archive, upload, submit, measure | release checklist |

## Human Touchpoints

Pause for the user at these points:

1. Target keyword approval.
2. Icon/visual direction approval.
3. IAP/App Store Connect product setup if monetized.
4. Privacy truth confirmation and support contact.
5. Final public submission confirmation.

## Ship Gate

Block release when any of these are true:

- build fails or the app crashes in the core flow,
- metadata exceeds App Store limits,
- keyword field repeats name/subtitle words or includes trademarks,
- screenshot set is missing required device classes,
- privacy answers do not match actual data collection,
- app claims features that are not implemented,
- secrets/signing material are committed,
- public submission lacks explicit confirmation.

