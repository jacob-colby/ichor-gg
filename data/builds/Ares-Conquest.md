---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.56
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.16
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.54
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.48
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.66
  - name: Stampede
    pick_rate: 0.12
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.72
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.59
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.57
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.83
  - name: Veve Charm
    pick_rate: 0.09
    win_rate: 0.88
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.42
    - name: Medallion
      pick_rate: 0.05
      win_rate: 0.78
  community_starters:
  - name: Selflessness
    pick_rate: 0.25
    win_rate: 0.61
  - name: Warrior's Axe
    pick_rate: 0.18
    win_rate: 0.51
  - name: Heroism
    pick_rate: 0.14
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-08-22'
  god_win_rate: 0.5736040609137056
  god_matches_won: 226
  god_matches_played: 394
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix, Erosion, Eye of
    Providence, Mantle Of Discord, Stone of Binding, Draconic Scale, Shifter''s Shield,
    Shield Splitter, Gluttonous Grimoire, Spectral Armor, Magi''s Cloak, Leviathan''s
    Hide, Pharaoh''s Curse, Eye of the Storm, Helm of Radiance, Soul Gem, Runeforged
    Hammer, Screeching Gargoyle, Shogun''s Ofuda, Midgardian Mail, Prophetic Cloak,
    Doublet of Binding, Void Shield, Ancile, Oni Hunter''s Garb, Spear of Desolation,
    Helm of Darkness, Xibalban Effigy, Gladiator''s Shield, Void Stone, Ethereal Staff,
    Hussar''s Wings.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.62
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.67
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Tahuti,
    Berserker''s Shield, Soul Gem, Ethereal Staff, Jotunn''s Revenge, Rod of Asclepius,
    Gluttonous Grimoire, Breastplate of Valor, Phoenix Feather, Chandra''s Grace,
    Erosion, Eye of Providence, Draconic Scale, Shifter''s Shield, Spectral Armor,
    Mantle Of Discord, Stone of Binding, Yogi''s Necklace, Shield Splitter, Leviathan''s
    Hide, Glorious Pridwen, Runeforged Hammer, Pharaoh''s Curse, Eye of the Storm,
    The Reaper, Shogun''s Ofuda, Midgardian Mail, Lifebinder, Helm of Radiance, Doublet
    of Binding, Spirit Robe, Void Shield, Magi''s Cloak, Ancile, Screeching Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.59
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.55
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Stone of
    Binding, Amanita Charm, Kinetic Cuirass, Soul Gem, Berserker''s Shield, Screeching
    Gargoyle, Spear of Desolation, The Crusher, Void Shield, Breastplate of Valor,
    Spear of the Magus, Void Stone, Obsidian Shard, Shield of the Phoenix, Avenging
    Blade, Mantle Of Discord, Heartseeker, Erosion, Shield Splitter, The Reaper, Eye
    of Providence, Spectral Armor, Draconic Scale, Shifter''s Shield, Doom Orb, The
    Cosmic Horror, Helm of Radiance, Runeforged Hammer, Leviathan''s Hide, The World
    Stone, Pharaoh''s Curse, Titan''s Bane, Magi''s Cloak, Silverbranch Bow, Dreamer''s
    Idol, Nimble Ring, Eye of the Storm.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.54
      win: 0.59
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.59
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Nimble Ring, Golden Blade, Gluttonous Grimoire, Breastplate of
    Valor, Pharaoh''s Curse, Shogun''s Ofuda, Tyrfing, Shield Splitter, Shield of
    the Phoenix, Soul Gem, Mantle Of Discord, Runeforged Hammer, Stone of Binding,
    Riptalon, Lernaean Bow, Silverbranch Bow, Spectral Armor, The Crusher, Death Metal,
    Erosion, Helm of Radiance, Hydra''s Lament, Eye of Providence, Eye of the Storm,
    Toxic Blade, Draconic Scale, Shifter''s Shield, Leviathan''s Hide, Magi''s Cloak,
    Screeching Gargoyle, Daybreak Gavel, Spear of Desolation, The Reaper, Spear of
    the Magus, Ethereal Staff.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.59
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.21
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.29
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Soul
    Gem, Berserker''s Shield, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle,
    Gluttonous Grimoire, Chronos'' Pendant, Shield Splitter, Mantle Of Discord, Stone
    of Binding, Prophetic Cloak, Erosion, Helm of Radiance, Runeforged Hammer, Eye
    of Providence, Gladiator''s Shield, Spectral Armor, Death Metal, Draconic Scale,
    Shifter''s Shield, Nimble Ring, Chandra''s Grace, Eye of the Storm, Arondight,
    Gem of Focus, Leviathan''s Hide, Pharaoh''s Curse, The Crusher, Magi''s Cloak,
    Ethereal Staff, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Totem of
    Death.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Berserker''s
    Shield, Shifter''s Shield, Jotunn''s Revenge, Breastplate of Valor, Shield of
    the Phoenix, Erosion, Eye of Providence, Mantle Of Discord, Stone of Binding,
    Draconic Scale, Shield Splitter, Gluttonous Grimoire, Spectral Armor, Magi''s
    Cloak, Leviathan''s Hide, Pharaoh''s Curse, Eye of the Storm, Helm of Radiance,
    Soul Gem, Runeforged Hammer, Screeching Gargoyle, Shogun''s Ofuda, Midgardian
    Mail, Prophetic Cloak, Doublet of Binding, Void Shield, Ancile, Oni Hunter''s
    Garb, Spear of Desolation, Helm of Darkness, Xibalban Effigy, Gladiator''s Shield,
    Void Stone, Ethereal Staff, Hussar''s Wings.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.59
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.0
      fit: 0.27
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.59
      pick: 0.15
      fit: 0.62
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.13
      fit: 0.67
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.59
      pick: 0.0
      fit: 0.67
  starter: *id001
---
