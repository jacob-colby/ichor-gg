---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.53
    win_rate: 0.58
    alternates:
    - name: Barbed Carver
      pick_rate: 0.16
      win_rate: 0.53
    - name: Bracer of The Abyss
      pick_rate: 0.05
      win_rate: 0.52
  - name: Shield of the Phoenix
    pick_rate: 0.22
    win_rate: 0.62
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.52
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.15
      win_rate: 0.56
    - name: Gladiator's Shield
      pick_rate: 0.13
      win_rate: 0.68
  - name: Dwarven Plate
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.63
    - name: Gladiator's Shield
      pick_rate: 0.1
      win_rate: 0.58
  - name: Kinetic Cuirass
    pick_rate: 0.06
    win_rate: 0.65
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.1
      win_rate: 0.58
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.6
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.59
    - name: Medal of Defense
      pick_rate: 0.04
      win_rate: 0.42
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.47
    win_rate: 0.66
  - name: Bluestone Pendant
    pick_rate: 0.34
    win_rate: 0.48
  - name: Bumba's Spear
    pick_rate: 0.09
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-08-10'
  god_win_rate: 0.5705378020265004
  god_matches_won: 732
  god_matches_played: 1283
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Gladiator's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire, Jotunn''s Revenge,
    Berserker''s Shield, The Crusher, Freya''s Tears, Breastplate of Valor, Oni Hunter''s
    Garb, Shield Splitter, Soul Gem, Hydra''s Lament, Runeforged Hammer, Erosion,
    Eye of the Storm, Eye of Providence, Spectral Armor, Draconic Scale, Pharaoh''s
    Curse, Death Metal, Leviathan''s Hide, Golden Blade, Spear of the Magus, Mantle
    Of Discord, Stone of Binding, Midgardian Mail, Helm of Radiance, Avenging Blade,
    Damaru, Lernaean Bow, Shogun''s Ofuda, The Reaper, The Cosmic Horror, Magi''s
    Cloak, Yogi''s Necklace, Screeching Gargoyle, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.59
      pick: 0.26
      fit: 0.28
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.65
      pick: 0.13
      fit: 0.61
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.3
      fit: 0.43
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.41
      win: 0.68
      pick: 0.2
      fit: 0.53
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.51
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Kinetic Cuirass, Gluttonous Grimoire, Jotunn''s Revenge, Soul Gem, The Crusher,
    Amanita Charm, Berserker''s Shield, Breastplate of Valor, Freya''s Tears, Spear
    of the Magus, Hydra''s Lament, Oni Hunter''s Garb, Spear of Desolation, The Cosmic
    Horror, Death Metal, Runeforged Hammer, Helm of Radiance, Shield Splitter, Obsidian
    Shard, Spectral Armor, Erosion, Pharaoh''s Curse, Chronos'' Pendant, Eye of Providence,
    Rod of Asclepius, Eye of the Storm, The Reaper, Draconic Scale, Jade Scepter,
    Leviathan''s Hide, Screeching Gargoyle, Riptalon, Golden Blade, Midgardian Mail,
    Damaru, Mantle Of Discord, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.59
      pick: 0.26
      fit: 0.27
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.13
      fit: 0.48
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.3
      fit: 0.38
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.41
      win: 0.68
      pick: 0.2
      fit: 0.48
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Soul Gem, Gluttonous Grimoire, Jotunn''s
    Revenge, Berserker''s Shield, The Crusher, The Reaper, Rod of Asclepius, Chandra''s
    Grace, Oni Hunter''s Garb, Breastplate of Valor, Runeforged Hammer, Freya''s Tears,
    Hydra''s Lament, Riptalon, Eye of the Storm, Shield Splitter, Phoenix Feather,
    Blood-Bound Book, Erosion, Spectral Armor, Bancroft''s Talon, Eye of Providence,
    Pharaoh''s Curse, Draconic Scale, Golden Blade, Lifebinder, Leviathan''s Hide,
    Death Metal, Avenging Blade, Spear of the Magus, Midgardian Mail, Yogi''s Necklace,
    Damaru, Shogun''s Ofuda, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.59
      pick: 0.26
      fit: 0.25
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.65
      pick: 0.13
      fit: 0.6
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.3
      fit: 0.74
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.41
      win: 0.68
      pick: 0.2
      fit: 0.54
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.5
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Shifter's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Amanita Charm, Soul Gem, Berserker''s Shield, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Breastplate of Valor, Freya''s Tears, Void Shield, Spear
    of the Magus, Oni Hunter''s Garb, The Cosmic Horror, Hydra''s Lament, Void Stone,
    The Reaper, Shield Splitter, Runeforged Hammer, Spear of Desolation, Erosion,
    Spectral Armor, Eye of Providence, Eye of the Storm, Heartseeker, Pharaoh''s Curse,
    Riptalon, Obsidian Shard, Draconic Scale, Death Metal, Silverbranch Bow, Leviathan''s
    Hide, Helm of Radiance, Golden Blade, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.59
      pick: 0.26
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.13
      fit: 0.52
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.3
      fit: 0.35
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.42
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Riptalon
  flex_slots:
  - Riptalon
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Berserker''s Shield, Gluttonous Grimoire, Amanita Charm,
    Jotunn''s Revenge, Riptalon, The Crusher, Golden Blade, Pharaoh''s Curse, Soul
    Gem, Breastplate of Valor, Oni Hunter''s Garb, Freya''s Tears, Silverbranch Bow,
    Lernaean Bow, Shogun''s Ofuda, Hydra''s Lament, Bracer of The Abyss, Runeforged
    Hammer, Spectral Armor, Tyrfing, Erosion, Shield Splitter, Spear of the Magus,
    Eye of Providence, Helm of Radiance, Draconic Scale, Eye of the Storm, Death Metal,
    Leviathan''s Hide, The Cosmic Horror, Toxic Blade, Yogi''s Necklace, Midgardian
    Mail, Mantle Of Discord, The Reaper, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.59
      pick: 0.26
      fit: 0.19
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.65
      pick: 0.13
      fit: 0.44
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.62
      pick: 0.3
      fit: 0.28
    Riptalon:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Jotunn''s Revenge,
    Breastplate of Valor, Soul Gem, Gluttonous Grimoire, Freya''s Tears, Amanita Charm,
    Berserker''s Shield, Hydra''s Lament, The Crusher, Oni Hunter''s Garb, Spear of
    Desolation, Screeching Gargoyle, Chronos'' Pendant, Chandra''s Grace, Erosion,
    Spectral Armor, Spear of the Magus, Eye of Providence, Pharaoh''s Curse, Runeforged
    Hammer, Shield Splitter, Helm of Radiance, Prophetic Cloak, Draconic Scale, The
    Cosmic Horror, Gem of Focus, Death Metal, Leviathan''s Hide, Eye of the Storm,
    Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Stone of Binding, Jade Scepter,
    Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.59
      pick: 0.26
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.13
      fit: 0.51
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.62
      pick: 0.3
      fit: 0.56
    Gladiator's Shield:
      total: 0.56
      efficiency: 0.41
      win: 0.68
      pick: 0.2
      fit: 0.66
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Kinetic Cuirass, Gluttonous Grimoire, Jotunn''s
    Revenge, Soul Gem, Amanita Charm, The Crusher, Berserker''s Shield, Breastplate
    of Valor, Freya''s Tears, Spear of the Magus, Death Metal, Hydra''s Lament, Oni
    Hunter''s Garb, The Cosmic Horror, Helm of Radiance, Spear of Desolation, Runeforged
    Hammer, Rod of Asclepius, Shield Splitter, Chronos'' Pendant, Jade Scepter, Obsidian
    Shard, Spectral Armor, Erosion, Bracer of The Abyss, Pharaoh''s Curse, Eye of
    Providence, Eye of the Storm, Blood-Bound Book, Bancroft''s Talon, Draconic Scale,
    Ethereal Staff, Wish-Granting Pearl, Leviathan''s Hide, Golden Blade, Damaru,
    Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.59
      pick: 0.26
      fit: 0.25
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.13
      fit: 0.49
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.3
      fit: 0.36
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.41
      win: 0.68
      pick: 0.2
      fit: 0.46
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Gladiator's Shield
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Gluttonous Grimoire,
    Jotunn''s Revenge, The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield,
    Breastplate of Valor, Freya''s Tears, Spear of the Magus, Oni Hunter''s Garb,
    Death Metal, Hydra''s Lament, Runeforged Hammer, The Cosmic Horror, Shield Splitter,
    Helm of Radiance, Spear of Desolation, Erosion, Eye of the Storm, Spectral Armor,
    Rod of Asclepius, Eye of Providence, Pharaoh''s Curse, Jade Scepter, Obsidian
    Shard, Draconic Scale, Chronos'' Pendant, Golden Blade, Damaru, Leviathan''s Hide,
    Lernaean Bow, The Reaper, Blood-Bound Book, Bancroft''s Talon, Midgardian Mail,
    Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.59
      pick: 0.26
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.13
      fit: 0.52
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.3
      fit: 0.35
    Gladiator's Shield:
      total: 0.53
      efficiency: 0.41
      win: 0.68
      pick: 0.2
      fit: 0.45
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.53
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Jotunn''s Revenge, Berserker''s Shield, The Crusher, Freya''s Tears, Breastplate
    of Valor, Oni Hunter''s Garb, Shield Splitter, Soul Gem, Hydra''s Lament, Runeforged
    Hammer, Erosion, Eye of the Storm, Eye of Providence, Spectral Armor, Draconic
    Scale, Pharaoh''s Curse, Death Metal, Leviathan''s Hide, Golden Blade, Spear of
    the Magus, Mantle Of Discord, Stone of Binding, Midgardian Mail, Helm of Radiance,
    Avenging Blade, Damaru, Lernaean Bow, Shogun''s Ofuda, The Reaper, The Cosmic
    Horror, Magi''s Cloak, Yogi''s Necklace, Screeching Gargoyle, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.59
      pick: 0.26
      fit: 0.28
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.59
      win: 0.65
      pick: 0.13
      fit: 0.61
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
---
