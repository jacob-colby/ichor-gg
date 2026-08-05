---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.55
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.31
    win_rate: 0.57
    alternates:
    - name: Eye of Erebus
      pick_rate: 0.18
      win_rate: 0.43
    - name: Devourer's Gauntlet
      pick_rate: 0.13
      win_rate: 0.44
  - name: Prophetic Cloak
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.26
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.46
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.38
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.27
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.43
  - name: Ethereal Staff
    pick_rate: 0.11
    win_rate: 0.25
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.54
    - name: Dwarven Plate
      pick_rate: 0.1
      win_rate: 0.36
  - name: Soul Reaver
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.17
    - name: Midgardian Mail
      pick_rate: 0.05
      win_rate: 0.2
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.2
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
    - name: Soul Reaver
      pick_rate: 0.06
      win_rate: 0.25
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-08-01'
  god_win_rate: 0.475
  god_matches_won: 57
  god_matches_played: 120
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Shifter's Shield
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Spectral Armor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Gluttonous Grimoire,
    Oni Hunter''s Garb, Spectral Armor, Shield of the Phoenix, Freya''s Tears, Mantle
    Of Discord, Breastplate of Valor, Erosion, Draconic Scale, Yogi''s Necklace, Leviathan''s
    Hide, Soul Gem, Midgardian Mail, Hussar''s Wings, Wish-Granting Pearl, Hide of
    the Nemean Lion, Jade Scepter, Bracer of The Abyss, Doublet of Binding, Rod of
    Asclepius, Chandra''s Grace, Ethereal Staff.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.68
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.37
    Shifter's Shield:
      total: 0.56
      efficiency: 0.58
      win: 0.57
      pick: 0.31
      fit: 0.58
    Spectral Armor:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.58
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Gluttonous Grimoire,
    Soul Gem, Eye of Providence, Rod of Asclepius, Chandra''s Grace, Oni Hunter''s
    Garb, Spectral Armor, Phoenix Feather, Erosion, Breastplate of Valor, Freya''s
    Tears, Draconic Scale, Yogi''s Necklace, Lifebinder, Bancroft''s Talon, Blood-Bound
    Book, Mantle Of Discord, Leviathan''s Hide, Spirit Robe, Wish-Granting Pearl,
    Jade Scepter, Ethereal Staff.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.8
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.39
    Shifter's Shield:
      total: 0.56
      efficiency: 0.58
      win: 0.57
      pick: 0.31
      fit: 0.56
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Gluttonous Grimoire
  - Shifter's Shield
  - Soul Reaver
  flex_slots:
  - Oni Hunter's Garb
  - Soul Reaver
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Soul Gem, Eye
    of Providence, Oni Hunter''s Garb, Spectral Armor, Stone of Binding, Void Shield,
    Breastplate of Valor, Shield of the Phoenix, Screeching Gargoyle, Spear of the
    Magus, Mantle Of Discord, Freya''s Tears, Void Stone, Yogi''s Necklace, Erosion,
    The Cosmic Horror, Draconic Scale, Leviathan''s Hide, Wish-Granting Pearl, Spear
    of Desolation, Jade Scepter, Ethereal Staff.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.52
    Oni Hunter's Garb:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.27
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.54
      efficiency: 0.58
      win: 0.57
      pick: 0.31
      fit: 0.42
    Soul Reaver:
      total: 0.51
      efficiency: 0.52
      win: 0.67
      pick: 0.06
      fit: 0.14
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Oni Hunter''s Garb,
    Eye of Providence, Spectral Armor, Breastplate of Valor, Soul Gem, Shield of the
    Phoenix, Mantle Of Discord, Yogi''s Necklace, Freya''s Tears, Erosion, Bracer
    of The Abyss, Bragi''s Harp, Draconic Scale, Death Metal, Leviathan''s Hide, Wish-Granting
    Pearl, Jade Scepter, Rod of Asclepius, Midgardian Mail, Nimble Ring, Chandra''s
    Grace, Ethereal Staff.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.47
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.23
    Nimble Ring:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.47
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.34
    Shifter's Shield:
      total: 0.53
      efficiency: 0.58
      win: 0.57
      pick: 0.31
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Soul Reaver
  flex_slots:
  - Freya's Tears
  - Soul Reaver
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Kinetic Cuirass,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Soul Gem, Freya''s
    Tears, Eye of Providence, Oni Hunter''s Garb, Spectral Armor, Chandra''s Grace,
    Mantle Of Discord, Chronos'' Pendant, Yogi''s Necklace, Gladiator''s Shield, Erosion,
    Wish-Granting Pearl, Jade Scepter, Draconic Scale, Death Metal, Screeching Gargoyle,
    Bracer of The Abyss, Rod of Asclepius, Leviathan''s Hide, Ethereal Staff.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.53
      efficiency: 0.58
      win: 0.57
      pick: 0.31
      fit: 0.39
    Soul Reaver:
      total: 0.51
      efficiency: 0.52
      win: 0.67
      pick: 0.06
      fit: 0.18
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: The Crusher, Berserker''s Shield, Gluttonous
    Grimoire, Jotunn''s Revenge, Runeforged Hammer, Kinetic Cuirass, Hydra''s Lament,
    Amanita Charm, Eye of Providence, Lernaean Bow, Oni Hunter''s Garb, Avenging Blade,
    Golden Blade, Shield Splitter, Eye of the Storm, Pharaoh''s Curse, Soul Gem, Spectral
    Armor, Breastplate of Valor, Shield of the Phoenix, Mantle Of Discord, Death Metal,
    Freya''s Tears, Damaru, The Reaper, Yogi''s Necklace, Erosion, Heartseeker, Draconic
    Scale, Shogun''s Ofuda, Bragi''s Harp, Triton''s Conch, Leviathan''s Hide, Arondight,
    Avatar''s Parashu, Wyrmskin Hide, Ethereal Staff.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.41
    Shifter's Shield:
      total: 0.54
      efficiency: 0.58
      win: 0.57
      pick: 0.31
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Soul Reaver
  flex_slots:
  - Soul Reaver
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Berserker''s
    Shield, The Crusher, Runeforged Hammer, Jotunn''s Revenge, Kinetic Cuirass, Amanita
    Charm, Hydra''s Lament, Soul Gem, Lernaean Bow, Oni Hunter''s Garb, Eye of Providence,
    Pharaoh''s Curse, Golden Blade, Avenging Blade, Death Metal, Spectral Armor, Shield
    Splitter, Bragi''s Harp, Breastplate of Valor, Wish-Granting Pearl, Eye of the
    Storm, Jade Scepter, Shield of the Phoenix, Mantle Of Discord, Yogi''s Necklace,
    Spear of the Magus, Rod of Asclepius, Bracer of The Abyss, Freya''s Tears, Triton''s
    Conch, Shogun''s Ofuda, Damaru, Helm of Radiance, Erosion, The Reaper, Ethereal
    Staff.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.36
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.53
      efficiency: 0.58
      win: 0.57
      pick: 0.31
      fit: 0.36
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Reaver:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.06
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Gluttonous
    Grimoire, Oni Hunter''s Garb, Spectral Armor, Shield of the Phoenix, Freya''s
    Tears, Mantle Of Discord, Breastplate of Valor, Erosion, Draconic Scale, Ethereal
    Staff, Yogi''s Necklace, Leviathan''s Hide, Soul Gem, Midgardian Mail, Hussar''s
    Wings, Wish-Granting Pearl, Hide of the Nemean Lion, Jade Scepter, Bracer of The
    Abyss, Doublet of Binding, Rod of Asclepius, Chandra''s Grace.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.49
      efficiency: 0.74
      win: 0.38
      pick: 0.22
      fit: 0.32
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.68
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.37
    Shifter's Shield:
      total: 0.56
      efficiency: 0.58
      win: 0.57
      pick: 0.31
      fit: 0.58
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.58
  starter: *id001
---
