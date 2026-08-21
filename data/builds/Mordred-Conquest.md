---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.52
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.53
    win_rate: 0.58
    alternates:
    - name: Barbed Carver
      pick_rate: 0.12
      win_rate: 0.48
    - name: Shield of the Phoenix
      pick_rate: 0.04
      win_rate: 0.55
  - name: Shield of the Phoenix
    pick_rate: 0.23
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.53
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.51
  - name: Gladiator's Shield
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.55
    - name: Shield of the Phoenix
      pick_rate: 0.13
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.58
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.61
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.64
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.74
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.73
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.48
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.68
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.49
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.39
    win_rate: 0.48
  - name: Bumba's Golden Dagger
    pick_rate: 0.09
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-08-21'
  god_win_rate: 0.5568942436412316
  god_matches_won: 416
  god_matches_played: 747
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Berserker''s
    Shield, Gluttonous Grimoire, Shield Splitter, Breastplate of Valor, The Crusher,
    Runeforged Hammer, Mantle Of Discord, Stone of Binding, Soul Gem, Eye of the Storm,
    Erosion, Eye of Providence, Death Metal, Draconic Scale, Spectral Armor, Hydra''s
    Lament, Spear of Desolation, Heartseeker, Helm of Radiance, Leviathan''s Hide,
    The Reaper, Pharaoh''s Curse, Golden Blade, Spear of the Magus, Magi''s Cloak,
    Avenging Blade, Nimble Ring, Obsidian Shard, Screeching Gargoyle, Shogun''s Ofuda,
    Midgardian Mail, Titan''s Bane, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.58
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.44
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.53
      fit: 0.48
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Breastplate of Valor
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Freya''s Tears, Jotunn''s Revenge, Gluttonous Grimoire, Amanita Charm,
    Berserker''s Shield, Soul Gem, Breastplate of Valor, Death Metal, The Crusher,
    Spear of Desolation, Shield Splitter, Spear of the Magus, Runeforged Hammer, Hydra''s
    Lament, Nimble Ring, Helm of Radiance, Obsidian Shard, Heartseeker, Mantle Of
    Discord, Stone of Binding, Ethereal Staff, Eye of the Storm, Rod of Asclepius,
    Wish-Granting Pearl, Doom Orb, Ancient Signet, The Reaper, Spectral Armor, The
    World Stone, Erosion, Chronos'' Pendant, Jade Scepter, Eye of Providence, Golden
    Blade, Avenging Blade, The Cosmic Horror, Draconic Scale.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.45
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.34
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Freya''s Tears, Jotunn''s Revenge, Gluttonous Grimoire, Amanita
    Charm, Soul Gem, Berserker''s Shield, Spear of Desolation, Breastplate of Valor,
    The Crusher, Spear of the Magus, Obsidian Shard, Death Metal, Shield Splitter,
    Runeforged Hammer, Helm of Radiance, Nimble Ring, Mantle Of Discord, Hydra''s
    Lament, Stone of Binding, Heartseeker, The Reaper, Spectral Armor, Eye of the
    Storm, Ethereal Staff, Erosion, Doom Orb, Rod of Asclepius, The Cosmic Horror,
    Screeching Gargoyle, Eye of Providence, Chronos'' Pendant, The World Stone, Draconic
    Scale, Titan''s Bane, Leviathan''s Hide, Pharaoh''s Curse, Dreamer''s Idol.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.47
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.33
  starter: *id001
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
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Rod of Tahuti, Jotunn''s Revenge, Soul
    Gem, Berserker''s Shield, The Reaper, Gluttonous Grimoire, Ethereal Staff, Rod
    of Asclepius, Runeforged Hammer, The Crusher, Breastplate of Valor, Shield Splitter,
    Chandra''s Grace, Phoenix Feather, Eye of the Storm, Riptalon, Yogi''s Necklace,
    Erosion, Spectral Armor, Death Metal, Mantle Of Discord, Stone of Binding, Hydra''s
    Lament, Eye of Providence, Golden Blade, Draconic Scale, Spear of Desolation,
    Heartseeker, Avenging Blade, Leviathan''s Hide, Pharaoh''s Curse, Spear of the
    Magus, Blood-Bound Book, Lifebinder, Helm of Radiance, Glorious Pridwen.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.57
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.6
      pick: 0.31
      fit: 0.72
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.38
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.77
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
  - Stone of Binding
  - Gluttonous Grimoire
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
    for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s Revenge, Stone of Binding,
    Gluttonous Grimoire, Amanita Charm, The Crusher, Berserker''s Shield, Soul Gem,
    Avenging Blade, Screeching Gargoyle, Void Shield, Breastplate of Valor, Spear
    of Desolation, Spear of the Magus, Heartseeker, Void Stone, Shield Splitter, The
    Reaper, Obsidian Shard, Runeforged Hammer, Mantle Of Discord, Titan''s Bane, Death
    Metal, Eye of the Storm, Erosion, Spectral Armor, Hydra''s Lament, Eye of Providence,
    Tekko-Kagi, Helm of Radiance, Draconic Scale, Silverbranch Bow, Doom Orb, The
    Cosmic Horror, Nimble Ring, Leviathan''s Hide, Pharaoh''s Curse.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.51
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.5
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Amanita Charm, Nimble Ring, Gluttonous Grimoire, Golden Blade, Breastplate of
    Valor, Pharaoh''s Curse, Soul Gem, Riptalon, Shogun''s Ofuda, Tyrfing, Silverbranch
    Bow, The Crusher, Shield Splitter, Runeforged Hammer, Mantle Of Discord, Stone
    of Binding, Lernaean Bow, Toxic Blade, Spectral Armor, Death Metal, Helm of Radiance,
    Erosion, Spear of the Magus, The Reaper, Spear of Desolation, Hydra''s Lament,
    Eye of Providence, Eye of the Storm, Tekko-Kagi, Leviathan''s Hide, Draconic Scale,
    Obsidian Shard, Magi''s Cloak, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.5
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.44
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.28
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s
    Revenge, Breastplate of Valor, Amanita Charm, Soul Gem, Berserker''s Shield, Spear
    of Desolation, Gluttonous Grimoire, Hydra''s Lament, Screeching Gargoyle, Mantle
    Of Discord, Stone of Binding, Chronos'' Pendant, Shield Splitter, The Crusher,
    Runeforged Hammer, Helm of Radiance, Spear of the Magus, Nimble Ring, Death Metal,
    Spectral Armor, Prophetic Cloak, Erosion, Eye of Providence, Obsidian Shard, Draconic
    Scale, Chandra''s Grace, Leviathan''s Hide, Eye of the Storm, Pharaoh''s Curse,
    Arondight, Gem of Focus, Ethereal Staff, Magi''s Cloak, Rod of Asclepius, Daybreak
    Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.27
      fit: 0.42
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.49
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.31
      fit: 0.53
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Spear of Desolation
  flex_slots:
  - Berserker's Shield
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s
    Revenge, Gluttonous Grimoire, Amanita Charm, Soul Gem, Berserker''s Shield, Spear
    of Desolation, Death Metal, Breastplate of Valor, Spear of the Magus, Helm of
    Radiance, Nimble Ring, The Crusher, Obsidian Shard, Shield Splitter, Runeforged
    Hammer, Ethereal Staff, Mantle Of Discord, Stone of Binding, Rod of Asclepius,
    Hydra''s Lament, Chronos'' Pendant, Eye of the Storm, Spectral Armor, Erosion,
    Jade Scepter, Doom Orb, Heartseeker, The Cosmic Horror, Wish-Granting Pearl, Eye
    of Providence, The Reaper, Ancient Signet, The World Stone, Draconic Scale, Leviathan''s
    Hide, Screeching Gargoyle.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.47
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Berserker''s Shield, Soul Gem, Death
    Metal, The Crusher, Breastplate of Valor, Shield Splitter, Spear of Desolation,
    Spear of the Magus, Runeforged Hammer, Helm of Radiance, Nimble Ring, Obsidian
    Shard, Mantle Of Discord, Stone of Binding, Eye of the Storm, Ethereal Staff,
    Hydra''s Lament, Rod of Asclepius, Heartseeker, Spectral Armor, Erosion, The Reaper,
    Eye of Providence, Draconic Scale, Jade Scepter, Doom Orb, Leviathan''s Hide,
    Golden Blade, The Cosmic Horror, Pharaoh''s Curse, Wish-Granting Pearl, Avenging
    Blade, Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.5
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.36
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.58
      pick: 0.53
      fit: 0.4
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Berserker''s
    Shield, Freya''s Tears, Gluttonous Grimoire, Shield Splitter, Breastplate of Valor,
    The Crusher, Runeforged Hammer, Mantle Of Discord, Stone of Binding, Soul Gem,
    Eye of the Storm, Erosion, Eye of Providence, Death Metal, Draconic Scale, Spectral
    Armor, Hydra''s Lament, Spear of Desolation, Heartseeker, Helm of Radiance, Leviathan''s
    Hide, The Reaper, Pharaoh''s Curse, Golden Blade, Spear of the Magus, Magi''s
    Cloak, Avenging Blade, Nimble Ring, Obsidian Shard, Screeching Gargoyle, Shogun''s
    Ofuda, Midgardian Mail, Titan''s Bane, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.64
      pick: 0.15
      fit: 0.58
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.73
      pick: 0.13
      fit: 0.44
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.6
      pick: 0.0
      fit: 0.18
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
  starter: *id001
---
