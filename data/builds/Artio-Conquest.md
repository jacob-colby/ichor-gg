---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.32
  aspect_win_rate: 0.52
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.36
    win_rate: 0.5
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.09
      win_rate: 0.48
    - name: Daybreak Gavel
      pick_rate: 0.07
      win_rate: 0.56
  - name: Breastplate of Valor
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.51
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.61
  - name: Genji's Guard
    pick_rate: 0.26
    win_rate: 0.54
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.5
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.45
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.54
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.41
  - name: Dwarven Plate
    pick_rate: 0.09
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.36
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.55
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.46
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.62
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.31
    win_rate: 0.5
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.64
  - name: Bumba's Hammer
    pick_rate: 0.11
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-08-10'
  god_win_rate: 0.5193370165745856
  god_matches_won: 282
  god_matches_played: 543
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Jotunn''s Revenge,
    Gluttonous Grimoire, Freya''s Tears, The Crusher, Oni Hunter''s Garb, Shield Splitter,
    Shield of the Phoenix, Hydra''s Lament, Draconic Scale, Runeforged Hammer, Erosion,
    Eye of the Storm, Eye of Providence, Spectral Armor, Pharaoh''s Curse, Soul Gem,
    Golden Blade, Leviathan''s Hide, Death Metal, Midgardian Mail, Mantle Of Discord,
    Avenging Blade, Stone of Binding, Helm of Radiance, Shogun''s Ofuda, Lernaean
    Bow, Damaru, Magi''s Cloak, Yogi''s Necklace, Ancile, Screeching Gargoyle, Rod
    of Asclepius, Void Shield, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.54
      pick: 0.4
      fit: 0.31
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.27
      fit: 0.31
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.56
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Berserker''s
    Shield, Gluttonous Grimoire, Jotunn''s Revenge, Rod of Asclepius, Chandra''s Grace,
    Oni Hunter''s Garb, The Crusher, Freya''s Tears, Runeforged Hammer, Hydra''s Lament,
    Eye of the Storm, Draconic Scale, The Reaper, Shield Splitter, Erosion, Phoenix
    Feather, Eye of Providence, Spectral Armor, Pharaoh''s Curse, Blood-Bound Book,
    Bancroft''s Talon, Golden Blade, Leviathan''s Hide, Riptalon, Lifebinder, Avenging
    Blade, Midgardian Mail, Death Metal, Shogun''s Ofuda, Glorious Pridwen, Yogi''s
    Necklace, Lernaean Bow, Helm of Radiance.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.54
      pick: 0.4
      fit: 0.28
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.8
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Soul Gem, Kinetic
    Cuirass, Amanita Charm, Berserker''s Shield, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Spear of the Magus, Void Shield, Freya''s Tears, Oni Hunter''s
    Garb, The Cosmic Horror, Hydra''s Lament, Void Stone, The Reaper, Shield of the
    Phoenix, Runeforged Hammer, Spear of Desolation, Shield Splitter, Draconic Scale,
    Riptalon, Spectral Armor, Obsidian Shard, Heartseeker, Erosion, Eye of the Storm,
    Pharaoh''s Curse, Eye of Providence, Silverbranch Bow, Death Metal, Golden Blade,
    Leviathan''s Hide, Helm of Radiance, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.54
      pick: 0.4
      fit: 0.22
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
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
    this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Golden Blade, Pharaoh''s Curse, Riptalon, Jotunn''s Revenge, The Crusher, Oni
    Hunter''s Garb, Freya''s Tears, Soul Gem, Lernaean Bow, Shogun''s Ofuda, Silverbranch
    Bow, Hydra''s Lament, Shield of the Phoenix, Tyrfing, Runeforged Hammer, Spectral
    Armor, Draconic Scale, Erosion, Shield Splitter, Bracer of The Abyss, Eye of Providence,
    Eye of the Storm, Leviathan''s Hide, Helm of Radiance, Eros'' Bow, Yogi''s Necklace,
    Death Metal, Midgardian Mail, Dominance, Spear of the Magus, Mantle Of Discord,
    Bragi''s Harp, Stone of Binding.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.54
      pick: 0.4
      fit: 0.19
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.34
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Freya''s Tears,
    Soul Gem, Shield of the Phoenix, Kinetic Cuirass, Gluttonous Grimoire, Amanita
    Charm, Hydra''s Lament, Berserker''s Shield, Oni Hunter''s Garb, Chronos'' Pendant,
    Screeching Gargoyle, The Crusher, Spear of Desolation, Chandra''s Grace, Gladiator''s
    Shield, Draconic Scale, Erosion, Spectral Armor, Prophetic Cloak, Eye of Providence,
    Pharaoh''s Curse, Runeforged Hammer, Gem of Focus, Shield Splitter, Helm of Radiance,
    Leviathan''s Hide, Eye of the Storm, Rod of Asclepius, Death Metal, Spear of the
    Magus, Midgardian Mail, Arondight, Jade Scepter, Mantle Of Discord, Stone of Binding,
    Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.54
      pick: 0.4
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.27
      fit: 0.48
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire, The
    Crusher, Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Hydra''s Lament,
    Soul Gem, Runeforged Hammer, Freya''s Tears, Oni Hunter''s Garb, Shield Splitter,
    Golden Blade, Pharaoh''s Curse, Lernaean Bow, Eye of the Storm, Shield of the
    Phoenix, Draconic Scale, Death Metal, Spectral Armor, Erosion, Spear of the Magus,
    The Reaper, Eye of Providence, Damaru, Shogun''s Ofuda, Avenging Blade, The Cosmic
    Horror, Riptalon, Leviathan''s Hide, Heartseeker, Helm of Radiance, Tekko-Kagi,
    Midgardian Mail, Silverbranch Bow, Yogi''s Necklace, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.54
      pick: 0.4
      fit: 0.22
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Soul Gem, Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Spear
    of the Magus, Freya''s Tears, Oni Hunter''s Garb, Death Metal, Hydra''s Lament,
    The Cosmic Horror, Runeforged Hammer, Helm of Radiance, Shield of the Phoenix,
    Shield Splitter, Spear of Desolation, Rod of Asclepius, Draconic Scale, Eye of
    the Storm, Spectral Armor, Erosion, Obsidian Shard, Jade Scepter, Pharaoh''s Curse,
    Eye of Providence, Chronos'' Pendant, Golden Blade, The Reaper, Blood-Bound Book,
    Lernaean Bow, Leviathan''s Hide, Damaru, Bancroft''s Talon, Ethereal Staff, Wish-Granting
    Pearl.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.54
      pick: 0.4
      fit: 0.22
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Jotunn''s Revenge, Gluttonous Grimoire, Freya''s Tears, The Crusher, Oni Hunter''s
    Garb, Shield Splitter, Shield of the Phoenix, Hydra''s Lament, Runeforged Hammer,
    Erosion, Eye of the Storm, Eye of Providence, Spectral Armor, Draconic Scale,
    Pharaoh''s Curse, Soul Gem, Golden Blade, Leviathan''s Hide, Death Metal, Midgardian
    Mail, Mantle Of Discord, Avenging Blade, Stone of Binding, Helm of Radiance, Shogun''s
    Ofuda, Lernaean Bow, Damaru, Magi''s Cloak, Yogi''s Necklace, Ancile, Screeching
    Gargoyle, Rod of Asclepius, Void Shield, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.54
      pick: 0.4
      fit: 0.31
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.56
  starter: *id001
---
