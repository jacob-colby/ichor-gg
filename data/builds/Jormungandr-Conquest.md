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
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Eye of Providence,
    Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Oni Hunter''s Garb, Pharaoh''s
    Curse, Runeforged Hammer, Freya''s Tears, Golden Blade, Shield Splitter, Hydra''s
    Lament, Lernaean Bow, Shield of the Phoenix, Eye of the Storm, Erosion, Shogun''s
    Ofuda, Spectral Armor, Breastplate of Valor, Draconic Scale, Soul Gem, Yogi''s
    Necklace, Avenging Blade, Death Metal, Leviathan''s Hide, Dominance, Helm of Radiance,
    Bragi''s Harp, Tyrfing, Rod of Asclepius, Stone of Binding, Mantle Of Discord,
    Hide of the Nemean Lion, Damaru, Bracer of The Abyss, Midgardian Mail.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.31
      fit: 0.48
    Amanita Charm:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Rod of Asclepius, Eye of Providence, Gluttonous Grimoire, Runeforged
    Hammer, Pharaoh''s Curse, Jotunn''s Revenge, Golden Blade, Oni Hunter''s Garb,
    The Crusher, Chandra''s Grace, Riptalon, Hydra''s Lament, The Reaper, Lernaean
    Bow, Freya''s Tears, Eye of the Storm, Shield Splitter, Shogun''s Ofuda, Blood-Bound
    Book, Phoenix Feather, Spectral Armor, Bancroft''s Talon, Erosion, Lifebinder,
    Yogi''s Necklace, Avenging Blade, Breastplate of Valor, Draconic Scale, Death
    Metal, Leviathan''s Hide, Dominance, Bragi''s Harp, Midgardian Mail.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.46
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shifter's Shield:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.31
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Avenging Blade, Soul Gem, Eye of Providence,
    Stone of Binding, Screeching Gargoyle, Oni Hunter''s Garb, Runeforged Hammer,
    Void Shield, Hydra''s Lament, Spear of the Magus, Pharaoh''s Curse, Freya''s Tears,
    Riptalon, Void Stone, Golden Blade, Lernaean Bow, Shield Splitter, The Cosmic
    Horror, Silverbranch Bow, The Reaper, Shield of the Phoenix, Breastplate of Valor,
    Spectral Armor, Tekko-Kagi, Yogi''s Necklace, Spear of Desolation, Eye of the
    Storm, Erosion, Shogun''s Ofuda, Heartseeker, Death Metal, Obsidian Shard.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shifter's Shield:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.31
      fit: 0.37
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher,
    Jotunn''s Revenge, Riptalon, Runeforged Hammer, Lernaean Bow, Freya''s Tears,
    Hydra''s Lament, Soul Gem, Shogun''s Ofuda, Tyrfing, Shield of the Phoenix, Shield
    Splitter, Breastplate of Valor, Silverbranch Bow, Spectral Armor, Yogi''s Necklace,
    Erosion, Eye of the Storm, Draconic Scale, Bracer of The Abyss, Dominance, Death
    Metal, Leviathan''s Hide, Rod of Asclepius, Helm of Radiance, Avenging Blade,
    Bragi''s Harp, Eros'' Bow, Hide of the Nemean Lion, Midgardian Mail.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
    Shifter's Shield:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.31
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.37
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Amanita Charm,
    Freya''s Tears, Jotunn''s Revenge, Kinetic Cuirass, Hydra''s Lament, Soul Gem,
    Gluttonous Grimoire, Shield of the Phoenix, Breastplate of Valor, Eye of Providence,
    Oni Hunter''s Garb, Pharaoh''s Curse, The Crusher, Runeforged Hammer, Chronos''
    Pendant, Screeching Gargoyle, Spectral Armor, Spear of Desolation, Golden Blade,
    Chandra''s Grace, Shield Splitter, Lernaean Bow, Erosion, Shogun''s Ofuda, Yogi''s
    Necklace, Gladiator''s Shield, Prophetic Cloak, Helm of Radiance, Rod of Asclepius,
    Draconic Scale, Eye of the Storm, Death Metal, Gem of Focus, Leviathan''s Hide,
    Arondight, Bracer of The Abyss, Spear of the Magus.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Hydra's Lament:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.31
      fit: 0.39
    Amanita Charm:
      total: 0.52
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence,
    Runeforged Hammer, Hydra''s Lament, Shield Splitter, Oni Hunter''s Garb, Freya''s
    Tears, Soul Gem, Golden Blade, Eye of the Storm, Lernaean Bow, Pharaoh''s Curse,
    Shield of the Phoenix, Death Metal, Avenging Blade, Breastplate of Valor, Spectral
    Armor, Erosion, The Reaper, Yogi''s Necklace, Spear of the Magus, Draconic Scale,
    Damaru, Shogun''s Ofuda, Leviathan''s Hide, Dominance, The Cosmic Horror, Helm
    of Radiance, Heartseeker, Tekko-Kagi, Rod of Asclepius, Tyrfing, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shifter's Shield:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.31
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.52
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Berserker''s
    Shield, Amanita Charm, The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Soul Gem,
    Eye of Providence, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s Lament, Pharaoh''s
    Curse, Death Metal, Spear of the Magus, Freya''s Tears, Golden Blade, Lernaean
    Bow, Shield Splitter, Rod of Asclepius, The Cosmic Horror, Helm of Radiance, Shield
    of the Phoenix, Breastplate of Valor, Bragi''s Harp, Eye of the Storm, Spectral
    Armor, Yogi''s Necklace, Bracer of The Abyss, Erosion, Jade Scepter, Shogun''s
    Ofuda, Spear of Desolation, Avenging Blade, Obsidian Shard, Riptalon, Draconic
    Scale, The Reaper, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.31
      fit: 0.36
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Eye of Providence, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Oni Hunter''s
    Garb, Pharaoh''s Curse, Runeforged Hammer, Freya''s Tears, Golden Blade, Shield
    Splitter, Hydra''s Lament, Breastplate of Valor, Lernaean Bow, Shield of the Phoenix,
    Eye of the Storm, Erosion, Shogun''s Ofuda, Spectral Armor, Draconic Scale, Soul
    Gem, Yogi''s Necklace, Avenging Blade, Death Metal, Leviathan''s Hide, Dominance,
    Midgardian Mail, Helm of Radiance, Bragi''s Harp, Tyrfing, Rod of Asclepius, Stone
    of Binding, Mantle Of Discord, Hide of the Nemean Lion, Damaru, Bracer of The
    Abyss.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.47
      efficiency: 0.72
      win: 0.38
      pick: 0.22
      fit: 0.26
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
---
