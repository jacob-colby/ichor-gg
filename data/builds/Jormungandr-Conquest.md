---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.68
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.33
    win_rate: 0.58
    alternates:
    - name: Eye of Erebus
      pick_rate: 0.15
      win_rate: 0.48
    - name: Devourer's Gauntlet
      pick_rate: 0.13
      win_rate: 0.71
  - name: Ethereal Staff
    pick_rate: 0.15
    win_rate: 0.45
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.63
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.14
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.54
  - name: Soul Reaver
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.14
      win_rate: 0.65
    - name: Gladiator's Shield
      pick_rate: 0.13
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.33
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.44
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 1.0
    alternates:
    - name: Soul Reliquary
      pick_rate: 0.05
      win_rate: 0.75
    - name: Spirit Robe
      pick_rate: 0.04
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.43
    win_rate: 0.51
  - name: Bluestone Pendant
    pick_rate: 0.25
    win_rate: 0.56
  - name: Heroism
    pick_rate: 0.07
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-08-15'
  god_win_rate: 0.5441176470588235
  god_matches_won: 74
  god_matches_played: 136
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-15'
  god_matches_analyzed: 4746
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Rod of Tahuti,
    The Crusher, Nimble Ring, Freya''s Tears, Jotunn''s Revenge, Gluttonous Grimoire,
    Pharaoh''s Curse, Breastplate of Valor, Oni Hunter''s Garb, Golden Blade, Shield
    of the Phoenix, Shield Splitter, Runeforged Hammer, Erosion, Hydra''s Lament,
    Eye of Providence, Eye of the Storm, Spectral Armor, Shogun''s Ofuda, Draconic
    Scale, Lernaean Bow, Soul Gem, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Death Metal, Avenging Blade, Tyrfing, Helm of Radiance, Damaru,
    Screeching Gargoyle, Ancile, Magi''s Cloak, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.26
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.58
    Hide of the Nemean Lion:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.31
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.57
      pick: 0.0
      fit: 0.09
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.48
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Berserker''s Shield, Kinetic Cuirass,
    Soul Gem, Rod of Tahuti, Gluttonous Grimoire, The Crusher, Nimble Ring, Chandra''s
    Grace, Jotunn''s Revenge, Rod of Asclepius, Golden Blade, Pharaoh''s Curse, Riptalon,
    Oni Hunter''s Garb, Runeforged Hammer, Freya''s Tears, The Reaper, Breastplate
    of Valor, Phoenix Feather, Hydra''s Lament, Eye of the Storm, Shogun''s Ofuda,
    Spectral Armor, Erosion, Shield Splitter, Eye of Providence, Lernaean Bow, Blood-Bound
    Book, Draconic Scale, Leviathan''s Hide, Bancroft''s Talon, Lifebinder, Avenging
    Blade, Midgardian Mail, Death Metal, Tyrfing, Glorious Pridwen.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.23
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.49
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.56
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.71
    Hide of the Nemean Lion:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.32
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, Jotunn''s Revenge,
    Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Soul Gem, Stone of Binding,
    Nimble Ring, Avenging Blade, Screeching Gargoyle, Void Shield, Freya''s Tears,
    Breastplate of Valor, Oni Hunter''s Garb, The Cosmic Horror, Void Stone, Pharaoh''s
    Curse, Riptalon, Spear of the Magus, Runeforged Hammer, Shield of the Phoenix,
    The Reaper, Golden Blade, Hydra''s Lament, Silverbranch Bow, Shield Splitter,
    Spectral Armor, Spear of Desolation, Erosion, Tekko-Kagi, Eye of Providence, Eye
    of the Storm, Shogun''s Ofuda, Lernaean Bow, Draconic Scale, Obsidian Shard, Toxic
    Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.2
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.24
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.57
      pick: 0.0
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Nimble Ring
  - Hide of the Nemean Lion
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
  - Golden Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Nimble Ring, Rod of Tahuti, Kinetic Cuirass, Amanita
    Charm, Gluttonous Grimoire, Golden Blade, The Crusher, Pharaoh''s Curse, Freya''s
    Tears, Jotunn''s Revenge, Breastplate of Valor, Riptalon, Oni Hunter''s Garb,
    Soul Gem, Shield of the Phoenix, Shogun''s Ofuda, Tyrfing, Runeforged Hammer,
    Spectral Armor, Erosion, Hydra''s Lament, Lernaean Bow, Silverbranch Bow, Shield
    Splitter, Eye of Providence, Draconic Scale, Eye of the Storm, Leviathan''s Hide,
    Midgardian Mail, Toxic Blade, Mantle Of Discord, Stone of Binding, Helm of Radiance,
    Death Metal, Screeching Gargoyle, Yogi''s Necklace, Damaru, Ancile.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.2
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.3
    Hide of the Nemean Lion:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.24
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.57
      pick: 0.0
      fit: 0.07
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Hide of the Nemean Lion
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Rod of Tahuti
  - Breastplate of Valor
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Berserker''s Shield,
    Rod of Tahuti, Breastplate of Valor, Jotunn''s Revenge, Kinetic Cuirass, Amanita
    Charm, Shield of the Phoenix, Soul Gem, Nimble Ring, Gluttonous Grimoire, Hydra''s
    Lament, The Crusher, Oni Hunter''s Garb, Pharaoh''s Curse, Screeching Gargoyle,
    Chronos'' Pendant, Chandra''s Grace, Spear of Desolation, Spectral Armor, Erosion,
    Runeforged Hammer, Eye of Providence, Golden Blade, Shogun''s Ofuda, Shield Splitter,
    Draconic Scale, Leviathan''s Hide, Helm of Radiance, Eye of the Storm, Midgardian
    Mail, Gem of Focus, Lernaean Bow, Mantle Of Discord, Stone of Binding, Death Metal,
    The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.41
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.41
    Hide of the Nemean Lion:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.25
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.57
      pick: 0.0
      fit: 0.12
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - The Crusher
  - Rod of Tahuti
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, The Crusher, Jotunn''s Revenge,
    Kinetic Cuirass, Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Freya''s
    Tears, Runeforged Hammer, Nimble Ring, Shield Splitter, Breastplate of Valor,
    Hydra''s Lament, Oni Hunter''s Garb, Soul Gem, Golden Blade, Eye of the Storm,
    Shield of the Phoenix, Pharaoh''s Curse, Erosion, Spectral Armor, Eye of Providence,
    The Reaper, Lernaean Bow, Draconic Scale, Death Metal, Avenging Blade, Damaru,
    The Cosmic Horror, Shogun''s Ofuda, Leviathan''s Hide, Midgardian Mail, Spear
    of the Magus, Mantle Of Discord, Stone of Binding, Tekko-Kagi, Spear of Desolation,
    Tyrfing, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.27
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.77
      win: 0.57
      pick: 0.0
      fit: 0.19
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - The Crusher
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Berserker''s Shield, Nimble Ring, The Crusher, Kinetic Cuirass, Jotunn''s Revenge,
    Amanita Charm, Soul Gem, Freya''s Tears, Breastplate of Valor, Oni Hunter''s Garb,
    Runeforged Hammer, The Cosmic Horror, Pharaoh''s Curse, Hydra''s Lament, Golden
    Blade, Shield of the Phoenix, Death Metal, Spear of the Magus, Shield Splitter,
    Spectral Armor, Helm of Radiance, Spear of Desolation, Erosion, Eye of the Storm,
    Lernaean Bow, Eye of Providence, Shogun''s Ofuda, Rod of Asclepius, Draconic Scale,
    Bragi''s Harp, Riptalon, Leviathan''s Hide, Chronos'' Pendant, The Reaper, Obsidian
    Shard, Jade Scepter, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.2
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.36
    Hide of the Nemean Lion:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.15
      fit: 0.23
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.57
      pick: 0.0
      fit: 0.28
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - The Crusher
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm,
    Rod of Tahuti, The Crusher, Nimble Ring, Freya''s Tears, Jotunn''s Revenge, Gluttonous
    Grimoire, Pharaoh''s Curse, Breastplate of Valor, Oni Hunter''s Garb, Golden Blade,
    Shield of the Phoenix, Shield Splitter, Runeforged Hammer, Erosion, Hydra''s Lament,
    Eye of Providence, Eye of the Storm, Spectral Armor, Shogun''s Ofuda, Draconic
    Scale, Lernaean Bow, Soul Gem, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Death Metal, Avenging Blade, Tyrfing, Helm of Radiance, Damaru,
    Screeching Gargoyle, Ancile, Magi''s Cloak, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.63
      pick: 0.2
      fit: 0.26
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.57
      pick: 0.0
      fit: 0.32
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.57
      pick: 0.0
      fit: 0.09
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.48
  starter: *id001
---
