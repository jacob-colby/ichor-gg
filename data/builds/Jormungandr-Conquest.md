---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.48
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.33
    win_rate: 0.57
    alternates:
    - name: Eye of Erebus
      pick_rate: 0.26
      win_rate: 0.5
    - name: Devourer's Gauntlet
      pick_rate: 0.08
      win_rate: 0.5
  - name: Prophetic Cloak
    pick_rate: 0.13
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.4
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.38
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.61
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.68
  - name: Ethereal Staff
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.48
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.49
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.45
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.7
    - name: Soul Reaver
      pick_rate: 0.07
      win_rate: 0.5
  - name: Soul Reaver
    pick_rate: 0.07
    win_rate: 0.71
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.62
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.42
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.39
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.3
    win_rate: 0.41
  - name: Death's Embrace
    pick_rate: 0.1
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-08-09'
  god_win_rate: 0.5241935483870968
  god_matches_won: 195
  god_matches_played: 372
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-09'
  god_matches_analyzed: 15881
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Soul Reaver
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Soul Reaver
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
    Gluttonous Grimoire, Jotunn''s Revenge, Oni Hunter''s Garb, The Crusher, Pharaoh''s
    Curse, Runeforged Hammer, Freya''s Tears, Breastplate of Valor, Hydra''s Lament,
    Golden Blade, Shield Splitter, Lernaean Bow, Shield of the Phoenix, Shogun''s
    Ofuda, Eye of the Storm, Erosion, Spectral Armor, Draconic Scale, Soul Gem, Yogi''s
    Necklace, Death Metal, Avenging Blade, Leviathan''s Hide, Dominance, Midgardian
    Mail, Helm of Radiance, Damaru, Rod of Asclepius, Mantle Of Discord, Bragi''s
    Harp, Stone of Binding, Hide of the Nemean Lion, Tyrfing, Bracer of The Abyss.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.48
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.33
      fit: 0.48
    Soul Reaver:
      total: 0.51
      efficiency: 0.46
      win: 0.71
      pick: 0.07
      fit: 0.15
    Amanita Charm:
      total: 0.53
      efficiency: 0.66
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
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Rod of Asclepius, Gluttonous Grimoire, Eye of Providence, Runeforged
    Hammer, Jotunn''s Revenge, Oni Hunter''s Garb, Pharaoh''s Curse, The Crusher,
    Golden Blade, Riptalon, Chandra''s Grace, Hydra''s Lament, The Reaper, Breastplate
    of Valor, Lernaean Bow, Freya''s Tears, Shogun''s Ofuda, Eye of the Storm, Shield
    Splitter, Blood-Bound Book, Phoenix Feather, Spectral Armor, Bancroft''s Talon,
    Yogi''s Necklace, Erosion, Lifebinder, Avenging Blade, Draconic Scale, Death Metal,
    Leviathan''s Hide, Dominance, Midgardian Mail, Bragi''s Harp.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
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
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.33
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.66
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
    for this god: Gluttonous Grimoire, Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Amanita Charm, Kinetic Cuirass, Avenging Blade, Soul Gem, Eye of Providence,
    Stone of Binding, Oni Hunter''s Garb, Screeching Gargoyle, Runeforged Hammer,
    Breastplate of Valor, Hydra''s Lament, Void Shield, Pharaoh''s Curse, Spear of
    the Magus, Freya''s Tears, Riptalon, Lernaean Bow, Golden Blade, Void Stone, The
    Cosmic Horror, Silverbranch Bow, Shield Splitter, The Reaper, Shield of the Phoenix,
    Spectral Armor, Yogi''s Necklace, Tekko-Kagi, Shogun''s Ofuda, Spear of Desolation,
    Eye of the Storm, Erosion, Heartseeker, Death Metal, Obsidian Shard.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
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
      efficiency: 0.55
      win: 0.57
      pick: 0.33
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
  - Gluttonous Grimoire
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher,
    Jotunn''s Revenge, Breastplate of Valor, Riptalon, Runeforged Hammer, Freya''s
    Tears, Lernaean Bow, Hydra''s Lament, Soul Gem, Shogun''s Ofuda, Shield of the
    Phoenix, Tyrfing, Spectral Armor, Silverbranch Bow, Yogi''s Necklace, Shield Splitter,
    Erosion, Eye of the Storm, Bracer of The Abyss, Draconic Scale, Dominance, Death
    Metal, Leviathan''s Hide, Rod of Asclepius, Helm of Radiance, Avenging Blade,
    Bragi''s Harp, Midgardian Mail, Damaru, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.34
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.33
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
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
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
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
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Breastplate of
    Valor, Amanita Charm, Freya''s Tears, Jotunn''s Revenge, Kinetic Cuirass, Hydra''s
    Lament, Gluttonous Grimoire, Soul Gem, Shield of the Phoenix, Eye of Providence,
    Oni Hunter''s Garb, Pharaoh''s Curse, The Crusher, Runeforged Hammer, Chronos''
    Pendant, Screeching Gargoyle, Prophetic Cloak, Spectral Armor, Chandra''s Grace,
    Golden Blade, Yogi''s Necklace, Lernaean Bow, Spear of Desolation, Shogun''s Ofuda,
    Erosion, Shield Splitter, Gladiator''s Shield, Helm of Radiance, Rod of Asclepius,
    Draconic Scale, Death Metal, Eye of the Storm, Gem of Focus, Leviathan''s Hide,
    Bracer of The Abyss, Arondight, Jade Scepter.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.33
      fit: 0.39
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
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
    Runeforged Hammer, Hydra''s Lament, Oni Hunter''s Garb, Shield Splitter, Breastplate
    of Valor, Freya''s Tears, Soul Gem, Golden Blade, Lernaean Bow, Eye of the Storm,
    Pharaoh''s Curse, Shield of the Phoenix, Death Metal, Spectral Armor, Avenging
    Blade, Erosion, Yogi''s Necklace, The Reaper, Damaru, Draconic Scale, Spear of
    the Magus, Shogun''s Ofuda, Leviathan''s Hide, Dominance, Heartseeker, The Cosmic
    Horror, Helm of Radiance, Rod of Asclepius, Riptalon, Midgardian Mail, Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.33
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Soul Reaver
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Berserker''s
    Shield, Amanita Charm, The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Soul Gem,
    Eye of Providence, Oni Hunter''s Garb, Runeforged Hammer, Hydra''s Lament, Breastplate
    of Valor, Pharaoh''s Curse, Death Metal, Freya''s Tears, Spear of the Magus, Lernaean
    Bow, Golden Blade, Shield Splitter, Rod of Asclepius, The Cosmic Horror, Helm
    of Radiance, Shield of the Phoenix, Spectral Armor, Yogi''s Necklace, Bragi''s
    Harp, Eye of the Storm, Bracer of The Abyss, Shogun''s Ofuda, Jade Scepter, Erosion,
    Spear of Desolation, Avenging Blade, Riptalon, Damaru, Draconic Scale, Obsidian
    Shard, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.33
      fit: 0.36
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Reaver:
      total: 0.52
      efficiency: 0.46
      win: 0.71
      pick: 0.07
      fit: 0.26
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Eye of Providence, Gluttonous Grimoire, Jotunn''s Revenge, Oni Hunter''s Garb,
    The Crusher, Pharaoh''s Curse, Runeforged Hammer, Freya''s Tears, Breastplate
    of Valor, Hydra''s Lament, Golden Blade, Shield Splitter, Lernaean Bow, Shield
    of the Phoenix, Shogun''s Ofuda, Eye of the Storm, Erosion, Spectral Armor, Draconic
    Scale, Soul Gem, Yogi''s Necklace, Death Metal, Avenging Blade, Leviathan''s Hide,
    Dominance, Midgardian Mail, Helm of Radiance, Damaru, Rod of Asclepius, Mantle
    Of Discord, Bragi''s Harp, Stone of Binding, Hide of the Nemean Lion, Tyrfing,
    Bracer of The Abyss.'
  slot_scores:
    Eye of Providence:
      total: 0.51
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.47
      efficiency: 0.72
      win: 0.38
      pick: 0.16
      fit: 0.26
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
---
