---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.33
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.21
    win_rate: 0.37
    alternates:
    - name: Ancient Signet
      pick_rate: 0.17
      win_rate: 0.63
    - name: Runeforged Hammer
      pick_rate: 0.08
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.36
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.23
      win_rate: 0.59
    - name: Gladiator's Shield
      pick_rate: 0.07
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.35
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.54
  - name: Obsidian Shard
    pick_rate: 0.17
    win_rate: 0.45
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.4
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.1
    win_rate: 0.55
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.5
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.29
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Shield
      pick_rate: 0.07
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.31
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.26
    win_rate: 0.68
  - name: Sands Of Time
    pick_rate: 0.18
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-15'
  god_win_rate: 0.5103448275862069
  god_matches_won: 74
  god_matches_played: 145
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
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Kinetic Cuirass, The Crusher,
    Amanita Charm, Gluttonous Grimoire, Jotunn''s Revenge, Golden Blade, Rod of Tahuti,
    Nimble Ring, Eye of the Storm, Oni Hunter''s Garb, Pharaoh''s Curse, Hydra''s
    Lament, Shield Splitter, Shield of the Phoenix, Avenging Blade, Spectral Armor,
    Lernaean Bow, Erosion, Breastplate of Valor, Eye of Providence, Death Metal, Shogun''s
    Ofuda, Draconic Scale, Soul Gem, Damaru, Leviathan''s Hide, Midgardian Mail, Tyrfing,
    Triton''s Conch, The Reaper, Rod of Asclepius, Yogi''s Necklace, Wyrmskin Hide,
    Bragi''s Harp, Ancile, Hide of the Nemean Lion, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.08
      fit: 0.56
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield of the Phoenix, Kinetic Cuirass,
    Berserker''s Shield, Soul Gem, Gluttonous Grimoire, The Crusher, Rod of Asclepius,
    Oni Hunter''s Garb, Jotunn''s Revenge, The Reaper, Rod of Tahuti, Chandra''s Grace,
    Eye of the Storm, Golden Blade, Pharaoh''s Curse, Erosion, Nimble Ring, Shield
    Splitter, Phoenix Feather, Eye of Providence, Spectral Armor, Draconic Scale,
    Riptalon, Breastplate of Valor, Hydra''s Lament, Shogun''s Ofuda, Avenging Blade,
    Leviathan''s Hide, Midgardian Mail, Blood-Bound Book, Lifebinder, Lernaean Bow,
    Bancroft''s Talon, Death Metal, Ancile, Damaru, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.64
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.71
    Runeforged Hammer:
      total: 0.58
      efficiency: 0.55
      win: 0.67
      pick: 0.08
      fit: 0.53
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Gluttonous Grimoire, Runeforged Hammer, Rod of Tahuti,
    Jotunn''s Revenge, Soul Gem, Berserker''s Shield, Avenging Blade, Kinetic Cuirass,
    Amanita Charm, The Reaper, The Cosmic Horror, Nimble Ring, Spear of the Magus,
    Void Shield, Riptalon, Stone of Binding, Screeching Gargoyle, Oni Hunter''s Garb,
    Tekko-Kagi, Silverbranch Bow, Golden Blade, Void Stone, Spear of Desolation, Hydra''s
    Lament, Breastplate of Valor, Heartseeker, Pharaoh''s Curse, Eye of the Storm,
    Toxic Blade, Spectral Armor, Shield of the Phoenix, Titan''s Bane, Shield Splitter,
    Lernaean Bow, Death Metal, Erosion, Pendulum Blade, Genji''s Guard.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.55
      win: 0.67
      pick: 0.08
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.5
      pick: 0.13
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Runeforged Hammer
  - Gluttonous Grimoire
  flex_slots:
  - Gluttonous Grimoire
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Nimble Ring, Golden Blade, Gluttonous
    Grimoire, Kinetic Cuirass, Riptalon, Rod of Tahuti, The Crusher, Amanita Charm,
    Pharaoh''s Curse, Tyrfing, Jotunn''s Revenge, Silverbranch Bow, Lernaean Bow,
    Oni Hunter''s Garb, Soul Gem, Shogun''s Ofuda, Breastplate of Valor, Toxic Blade,
    Spectral Armor, Hydra''s Lament, Shield of the Phoenix, Eye of the Storm, Erosion,
    Eros'' Bow, Shield Splitter, Bragi''s Harp, Leviathan''s Hide, Eye of Providence,
    Death Metal, Avenging Blade, Bracer of The Abyss, Dominance, Midgardian Mail,
    The Reaper, Yogi''s Necklace, Damaru, Genji''s Guard.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.39
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.36
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.08
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Runeforged Hammer, Jotunn''s Revenge,
    Soul Gem, Breastplate of Valor, Shield of the Phoenix, Gluttonous Grimoire, Hydra''s
    Lament, Berserker''s Shield, Rod of Tahuti, Gladiator''s Shield, Kinetic Cuirass,
    Nimble Ring, Amanita Charm, The Crusher, Chronos'' Pendant, Chandra''s Grace,
    Spear of Desolation, Screeching Gargoyle, Oni Hunter''s Garb, Pharaoh''s Curse,
    Gem of Focus, Spectral Armor, Golden Blade, Totem of Death, Arondight, Erosion,
    Genji''s Guard, Rod of Asclepius, Death Metal, Prophetic Cloak, Eye of the Storm,
    The Cosmic Horror, Eye of Providence, Leviathan''s Hide, Shogun''s Ofuda, Helm
    of Radiance, Midgardian Mail, Spear of the Magus, Jade Scepter.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.55
      win: 0.67
      pick: 0.08
      fit: 0.34
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.25
      fit: 0.52
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.14
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Rod of Tahuti
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Kinetic Cuirass, The Crusher, Amanita
    Charm, Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge, Runeforged Hammer,
    Golden Blade, Genji''s Guard, Nimble Ring, Eye of the Storm, Oni Hunter''s Garb,
    Pharaoh''s Curse, Hydra''s Lament, Shield Splitter, Shield of the Phoenix, Avenging
    Blade, Spectral Armor, Lernaean Bow, Erosion, Breastplate of Valor, Eye of Providence,
    Death Metal, Shogun''s Ofuda, Draconic Scale, Damaru, Leviathan''s Hide, Soul
    Gem, Midgardian Mail, Tyrfing, Triton''s Conch, The Reaper, Rod of Asclepius,
    Yogi''s Necklace, Wyrmskin Hide, Bragi''s Harp, Ancile, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.55
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.77
      win: 0.5
      pick: 0.13
      fit: 0.12
    Amanita Charm:
      total: 0.53
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.45
  starter: *id001
---
