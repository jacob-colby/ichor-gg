---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.6
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.21
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.47
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.75
  - name: Genji's Guard
    pick_rate: 0.14
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.46
    - name: Prophetic Cloak
      pick_rate: 0.09
      win_rate: 0.47
  - name: Stampede
    pick_rate: 0.11
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.46
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.09
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.7
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.38
    - name: Gladiator's Shield
      pick_rate: 0.05
      win_rate: 0.86
  - name: Sundering Echo
    pick_rate: 0.08
    win_rate: 0.83
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.4
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.44
  - name: Warrior's Axe
    pick_rate: 0.18
    win_rate: 0.41
  - name: Selflessness
    pick_rate: 0.13
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-08-15'
  god_win_rate: 0.5193370165745856
  god_matches_won: 94
  god_matches_played: 181
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
  - Kinetic Cuirass
  - Prophetic Cloak
  - Gladiator's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gladiator''s Shield, Prophetic Cloak, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, Rod of Tahuti, Erosion, Gluttonous Grimoire, Shield of the Phoenix,
    Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Breastplate of Valor, Spectral
    Armor, Shield Splitter, Jotunn''s Revenge, Pharaoh''s Curse, The Crusher, Leviathan''s
    Hide, Mantle Of Discord, Midgardian Mail, Stone of Binding, Soul Gem, Eye of the
    Storm, Nimble Ring, Magi''s Cloak, Runeforged Hammer, Ancile, Shogun''s Ofuda,
    Screeching Gargoyle, Void Shield, Helm of Radiance, Doublet of Binding, Hydra''s
    Lament, Hussar''s Wings, Chandra''s Grace, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.53
      pick: 0.15
      fit: 0.78
    Prophetic Cloak:
      total: 0.59
      efficiency: 0.43
      win: 0.75
      pick: 0.13
      fit: 0.62
    Gladiator's Shield:
      total: 0.64
      efficiency: 0.41
      win: 0.86
      pick: 0.11
      fit: 0.67
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.08
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.68
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Prophetic Cloak
  - Shield of the Phoenix
  - Gladiator's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Gladiator''s Shield, Amanita Charm, Shield of the Phoenix, Soul Gem,
    Berserker''s Shield, Gluttonous Grimoire, Chandra''s Grace, Rod of Tahuti, Rod
    of Asclepius, Oni Hunter''s Garb, Erosion, Eye of Providence, Freya''s Tears,
    Phoenix Feather, Draconic Scale, Spectral Armor, Breastplate of Valor, Jotunn''s
    Revenge, Pharaoh''s Curse, Leviathan''s Hide, The Crusher, Midgardian Mail, Runeforged
    Hammer, Eye of the Storm, Glorious Pridwen, Lifebinder, Shield Splitter, Nimble
    Ring, Ancile, Blood-Bound Book, The Reaper, Shogun''s Ofuda, Void Shield, Doublet
    of Binding, Mantle Of Discord, Stone of Binding, Bancroft''s Talon, Hide of the
    Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.53
      pick: 0.15
      fit: 0.76
    Prophetic Cloak:
      total: 0.57
      efficiency: 0.43
      win: 0.75
      pick: 0.13
      fit: 0.54
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.9
    Gladiator's Shield:
      total: 0.64
      efficiency: 0.41
      win: 0.86
      pick: 0.11
      fit: 0.7
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Kinetic Cuirass
  - Prophetic Cloak
  - Gladiator's Shield
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge,
    Amanita Charm, Soul Gem, Stone of Binding, Berserker''s Shield, Screeching Gargoyle,
    Void Shield, The Cosmic Horror, Freya''s Tears, Oni Hunter''s Garb, Void Stone,
    Spear of the Magus, Shield of the Phoenix, Breastplate of Valor, Spear of Desolation,
    Avenging Blade, Erosion, Eye of Providence, Spectral Armor, Nimble Ring, Draconic
    Scale, The Reaper, Obsidian Shard, Pharaoh''s Curse, Riptalon, Shield Splitter,
    Leviathan''s Hide, Runeforged Hammer, Midgardian Mail, Silverbranch Bow, Mantle
    Of Discord, Hydra''s Lament, Eye of the Storm, Helm of Radiance, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.15
      fit: 0.58
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.43
      win: 0.75
      pick: 0.13
      fit: 0.43
    Gladiator's Shield:
      total: 0.61
      efficiency: 0.41
      win: 0.86
      pick: 0.11
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Prophetic Cloak
  - Gladiator's Shield
  - Nimble Ring
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Nimble Ring, Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Golden Blade, The Crusher, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon,
    Oni Hunter''s Garb, Breastplate of Valor, Freya''s Tears, Soul Gem, Shield of
    the Phoenix, Shogun''s Ofuda, Tyrfing, Runeforged Hammer, Spectral Armor, Erosion,
    Hydra''s Lament, Lernaean Bow, Silverbranch Bow, Shield Splitter, Eye of Providence,
    Draconic Scale, Eye of the Storm, Leviathan''s Hide, Midgardian Mail, Toxic Blade,
    Mantle Of Discord, Stone of Binding, Helm of Radiance, Death Metal, Screeching
    Gargoyle, Yogi''s Necklace, Damaru, Ancile.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.15
      fit: 0.47
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.43
      win: 0.75
      pick: 0.13
      fit: 0.33
    Gladiator's Shield:
      total: 0.6
      efficiency: 0.41
      win: 0.86
      pick: 0.11
      fit: 0.4
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Prophetic Cloak
  - Gladiator's Shield
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gladiator''s Shield, Prophetic Cloak,
    Freya''s Tears, Jotunn''s Revenge, Shield of the Phoenix, Rod of Tahuti, Breastplate
    of Valor, Amanita Charm, Soul Gem, Gluttonous Grimoire, Hydra''s Lament, Berserker''s
    Shield, The Crusher, Screeching Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant,
    Nimble Ring, Chandra''s Grace, Spear of Desolation, Erosion, Spectral Armor, Eye
    of Providence, Shield Splitter, Draconic Scale, Runeforged Hammer, Pharaoh''s
    Curse, Eye of the Storm, Leviathan''s Hide, Gem of Focus, Helm of Radiance, Midgardian
    Mail, Mantle Of Discord, Totem of Death, Stone of Binding, Arondight, Death Metal,
    Rod of Asclepius, The Cosmic Horror.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.48
      pick: 0.19
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.53
      pick: 0.15
      fit: 0.55
    Prophetic Cloak:
      total: 0.59
      efficiency: 0.43
      win: 0.75
      pick: 0.13
      fit: 0.64
    Gladiator's Shield:
      total: 0.64
      efficiency: 0.41
      win: 0.86
      pick: 0.11
      fit: 0.71
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.08
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Prophetic Cloak
  - Gladiator's Shield
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
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
    Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Runeforged Hammer, Nimble
    Ring, Shield Splitter, Hydra''s Lament, Oni Hunter''s Garb, Soul Gem, Freya''s
    Tears, Golden Blade, Eye of the Storm, Shield of the Phoenix, Breastplate of Valor,
    Pharaoh''s Curse, Erosion, Spectral Armor, Eye of Providence, The Reaper, Lernaean
    Bow, Draconic Scale, Death Metal, Avenging Blade, Damaru, The Cosmic Horror, Shogun''s
    Ofuda, Leviathan''s Hide, Midgardian Mail, Spear of the Magus, Mantle Of Discord,
    Stone of Binding, Tekko-Kagi, Spear of Desolation, Helm of Radiance, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.15
      fit: 0.52
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.43
      win: 0.75
      pick: 0.13
      fit: 0.38
    Gladiator's Shield:
      total: 0.6
      efficiency: 0.41
      win: 0.86
      pick: 0.11
      fit: 0.45
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.19
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Kinetic Cuirass
  - Prophetic Cloak
  - Gladiator's Shield
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    The Crusher, Jotunn''s Revenge, Amanita Charm, Soul Gem, Berserker''s Shield,
    Nimble Ring, Oni Hunter''s Garb, The Cosmic Horror, Freya''s Tears, Runeforged
    Hammer, Shield Splitter, Shield of the Phoenix, Death Metal, Breastplate of Valor,
    Spear of the Magus, Hydra''s Lament, Erosion, Spear of Desolation, Eye of the
    Storm, Helm of Radiance, Spectral Armor, Eye of Providence, Draconic Scale, Rod
    of Asclepius, Pharaoh''s Curse, The Reaper, Obsidian Shard, Leviathan''s Hide,
    Golden Blade, Chronos'' Pendant, Jade Scepter, Midgardian Mail, Avenging Blade,
    Mantle Of Discord, Damaru, Stone of Binding.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.15
      fit: 0.52
    Prophetic Cloak:
      total: 0.55
      efficiency: 0.43
      win: 0.75
      pick: 0.13
      fit: 0.38
    Gladiator's Shield:
      total: 0.6
      efficiency: 0.41
      win: 0.86
      pick: 0.11
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Freya''s Tears, Berserker''s Shield, Rod
    of Tahuti, Erosion, Gluttonous Grimoire, Shield of the Phoenix, Eye of Providence,
    Oni Hunter''s Garb, Breastplate of Valor, Draconic Scale, Spectral Armor, Shield
    Splitter, Jotunn''s Revenge, Pharaoh''s Curse, The Crusher, Leviathan''s Hide,
    Mantle Of Discord, Midgardian Mail, Stone of Binding, Soul Gem, Eye of the Storm,
    Nimble Ring, Magi''s Cloak, Runeforged Hammer, Ancile, Gladiator''s Shield, Shogun''s
    Ofuda, Screeching Gargoyle, Hide of the Nemean Lion, Prophetic Cloak, Void Shield,
    Helm of Radiance, Doublet of Binding, Hydra''s Lament, Hussar''s Wings, Chandra''s
    Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.48
      pick: 0.19
      fit: 0.37
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.53
      pick: 0.15
      fit: 0.78
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.08
      fit: 0.62
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.77
      win: 0.53
      pick: 0.0
      fit: 0.13
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.68
  starter: *id001
---
